
from collections import namedtuple
from functools import reduce
from datetime import timedelta
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
import logging
from django.backend import AuthFailedLoggerBackend
from django.signals import password_has_expired, password_will_expire_warning, account_has_expired

logger = logging.getLogger("django.security")

__all__ = ["AccountExpiryBackend"]


@receiver(pre_save, sender=settings.AUTH_USER_MODEL)
def user_pre_save(sender, instance=None, raw=False, **kwargs):
    user = instance
    attrs = ExpirySettings.get()
    # We're saving the password change date only for existing users
    # Users just created should be taken care of by auto_now_add.
    # This way we can assume that a User profile object already exists
    # for the user. This is essential, because password change detection
    # can happen only in pre_save, in post_save it is too late.
    is_new_user = user.pk is None
    if is_new_user or raw:
        return
    if attrs.date_changed:
        update_date_changed(user, attrs.date_changed)

    # User has been re-activated. Ensure the last_login is set to None so
    # that the user isn't inactivated on next login by the AccountExpiryBackend
    current_user = sender.objects.get(pk=user.pk)
    if not current_user.is_active and user.is_active:
        user.last_login = None


def update_date_changed(user, date_changed_attr):
    def did_password_change(user):
        current_user = get_user_model().objects.get(pk=user.pk)
        return current_user.password != user.password

    def save_profile_password_change_date(user, date):
        parts = date_changed_attr.split('.')
        attr_name = parts[-1]
        profile = reduce(lambda obj, attr: getattr(obj, attr), parts[:-1], user)
        setattr(profile, attr_name, date)
        profile.save()

    def set_password_change_date(user, date):
        setattr(user, date_changed_attr, date)

    if did_password_change(user):
        now = timezone.now()
        if '.' in date_changed_attr:
            save_profile_password_change_date(user, now)
        else:
            set_password_change_date(user, now)


def should_warn_about_password_expiry(user):
    warn_in_days = ExpirySettings.get().num_warning_days or 0
    days_left = days_to_password_expiry(user) or 0
    return warn_in_days > 0 and days_left <= warn_in_days


def days_to_password_expiry(user):
    earliest = ExpirySettings.get().earliest_possible_password_change
    if earliest:
        change_date = get_password_change_date(user)
        if change_date:
            return (change_date - earliest).days


def is_password_expired(user):
    days = days_to_password_expiry(user)
    return days is not None and days < 0


def get_password_change_date(user):
    attr = ExpirySettings.get().date_changed
    if attr:
        val = user
        if isinstance(attr, str):
            for part in attr.split("."):
                if hasattr(val, part):
                    val = getattr(val, part)
                else:
                    logger.warning("User model does not have a %s attribute" % attr)
                    return None
            return val
        else:
            logger.warning("Password change attr in settings is not a string")


def get_user_last_login(user):
    if hasattr(user, "last_login"):
        return user.last_login
    else:
        logger.warning("User model doesn't have last_login field. ACCOUNT_EXPIRY_DAYS setting will have no effect.")
        return None


def is_account_expired(user):
    earliest = ExpirySettings.get().earliest_possible_login
    if earliest:
        last_login = get_user_last_login(user)
        return last_login and last_login < earliest
    return False


class ExpirySettings(namedtuple("ExpirySettings",
                                ["num_days", "num_warning_days", "date_changed", "password", "account_expiry"])):
    @classmethod
    def get(cls):
        expiry = getattr(settings, "PASSWORD_EXPIRY_DAYS", None) or 0
        warning = getattr(settings, "PASSWORD_EXPIRY_WARNING_DAYS", None) or 0
        date_changed = getattr(settings, "AUTH_USER_MODEL_PASSWORD_CHANGE_DATE_ATTR", None) or None
        password = getattr(settings, "AUTH_USER_MODEL_PASSWORD_ATTR", None) or "password"
        account_expiry = getattr(settings, "ACCOUNT_EXPIRY_DAYS", None) or 0
        return cls(expiry, warning, date_changed, password, account_expiry)

    @property
    def earliest_possible_login(self):
        if self.account_expiry > 0:
            return timezone.now() - timedelta(days=self.account_expiry)
        return None

    @property
    def earliest_possible_password_change(self):
        if self.num_days > 0:
            return timezone.now() - timedelta(days=self.num_days)
        return None


class AccountExpiryBackend(object):
    """
    This backend doesn't authenticate, it just prevents authentication
    of a user whose account password has expired.
    """
    def authenticate(self, request=None, username=None, password=None, **kwargs):
        user = self._lookup_user(username, password, **kwargs)

        if user:
            # Prevent authentication of inactive users (if the user
            # model supports it). Django only checks is_active at the
            # login view level.
            if hasattr(user, "is_active") and not user.is_active:
                self._prevent_login(username, "Account is not active")

            if is_password_expired(user):
                logger.info("Password expired! Disabling user account: %s" % user)
                user.is_active = False
                user.save()
                password_has_expired.send(sender=user.__class__, user=user)
                self._prevent_login(username, "Password has expired")

            if is_account_expired(user):
                logger.info("Disabling stale user account: %s" % user)
                user.is_active = False
                user.save()
                account_has_expired.send(sender=user.__class__, user=user)
                self._prevent_login(username, "Account has expired")

            if should_warn_about_password_expiry(user):
                days_left = days_to_password_expiry(user)
                logger.info("User's '%s' password will expire in %d days", user, days_left)
                password_will_expire_warning.send(sender=user.__class__, user=user, days_left=days_left)

        # pass on to next handler
        return None

    def _prevent_login(self, username, msg="User login prevented"):
        def is_failed_login_logger_configured():
            auth_backends = getattr(settings, 'AUTHENTICATION_BACKENDS', [])
            return 'useraudit.backend.AuthFailedLoggerBackend' in auth_backends

        logger.info("Login Prevented for user '%s'! %s", username, msg)
        if is_failed_login_logger_configured():
            AuthFailedLoggerBackend().authenticate(username=username)
        raise PermissionDenied(msg)

    def _lookup_user(self, username=None, password=None, **kwargs):
        # This is the same procedure as in
        # django.contrib.auth.backends.ModelBackend, except without
        # the timing attack mitigation, because it doesn't take long
        # to check for expiry.
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            return UserModel._default_manager.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            return None