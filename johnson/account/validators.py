import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _, ngettext

from .models import Entity


class MinimumLengthValidator:
    """
    Validate whether the password is of a minimum length.
    """

    def __init__(self, min_length=0):
        self.min_length = min_length
        m = Entity.objects.filter(EID=4).values('MinChar')[0]
        min_length = m.get('MinChar')
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "This password is too short. It must contain at least %(min_length)d character.",
                    "This password is too short. It must contain at least %(min_length)d characters.",
                    self.min_length
                ),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return ngettext(
            "Your password must contain at least %(min_length)d character.",
            "Your password must contain at least %(min_length)d characters.",
            self.min_length
        ) % {'min_length': self.min_length}


class MaximumLengthValidator:
    """
    Validate whether the password is of a minimum length.
    """

    def __init__(self, min_length=8, max_length=None):
        self.min_length = min_length
        self.max_length = max_length
        m = Entity.objects.filter(EID=1).values('MaxChar')[0]
        max_char = m.get('MaxChar')
        self.max_length = max_char

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise ValidationError(
                ngettext(
                    "This password is too long. It must contain at least %(max_length)d character.",
                    "This password is too long. It must contain at least %(max_length)d characters.",
                    self.min_length
                ),
                code='password_too_long',
                params={'max_length': self.max_length},
            )


class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("The password must contain at least 1 digit, 0-9."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 digit, 0-9."
        )


class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("The password must contain at least 1 uppercase letter, A-Z."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 uppercase letter, A-Z."
        )


class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("The password must contain at least 1 lowercase letter, a-z."),
                code='password_no_lower',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 lowercase letter, a-z."
        )


class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("The password must contain at least 1 symbol: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 symbol: " +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )


from datetime import date, timedelta
from django.contrib.auth import authenticate, login

class PasswordExpireDays(object):
    def __init__(self, passexpiredays=0):
        self.passexpiredays=passexpiredays
        Passexpdays = Entity.objects.filter(EID=1).values('Passexpdays')[0]
        self.passexpiredays=Passexpdays


    def validate(self, password, user=None):
        if user.is_active():
            if date.today() - user.password_date > timedelta(days=self.passexpiredays):
                return


        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "This password is too short. It must contain at least %(min_length)d character.",
                    "This password is too short. It must contain at least %(min_length)d characters.",
                    self.min_length
                ),
                code='password_too_short',
                params={'min_length': self.min_length},
            )
