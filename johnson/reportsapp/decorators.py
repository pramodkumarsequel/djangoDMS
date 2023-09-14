from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from account.models import RoleMaster, User
from reportsapp.models import MenuMaster
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import permission_required



@permission_required
def unauthenitcated_user(views_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return views_func(request, *args, **kwargs)


    return wrapper_func

def allowed_users(allowed_roles=['']):
    def decorators(view_func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists() and request.user.role in allowed_roles:
                print(request.user.role)
                print(request.user.groups)
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper
    return decorators


def role_required(allow_roles=[]):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            us = request.user.role
            try:
                mn = MenuMaster.objects.get(Roles=us) 
                if mn.Is_Create:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse("You are not authorized to create record")        
            except ObjectDoesNotExist:
                mn = None
                return HttpResponse("You are not authorized to create record")
                
        return wrap
    return decorator 



from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate
from django.contrib.auth.decorators import user_passes_test
import functools
from django.shortcuts import redirect
from django.contrib import messages

def menu_show_as_per_role(request):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            us = request.user
            us_id = request.user.id
            us_role_id = request.user.role.id
            try:
                usrole = MenuMaster.objects.filter(id=us_role_id)
                current_user_role = MenuMaster.objects.filter(id__in=usrole)
                request.session['currentrole'] = current_user_role
                print(request.session['currentrole'])
                mn = MenuMaster.objects.get(Roles=us) 
                if mn.Is_View:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse("You are not authorized to create record")        
            except ObjectDoesNotExist:
                mn = None
                return HttpResponse("You are not authorized to create record")
                
        return wrap
    return decorator 


def perm_required(view_func):
    """
        this decorator ensures that a user is not logged in,
        if a user is logged in, the user get permission to create record if  
        user in role assignment get permission to can_create record 
    """
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        role = None
        try:
            role = MenuMaster.objects.filter(usrole=request.user.role)
            if role.Is_Create: 
                return view_func(request,*args, **kwargs)
        except ObjectDoesNotExist:
            role = None     
        messages.error(request, 'You are not authorize for this action.')
        return redirect('/home/')
    return wrapper
  





def check_perm_required(view_func, redirect_url="/home/"):
    """
        this decorator ensures that a user is not logged in,
        if a user is logged in, the user will get redirected to 
        the url whose view name was passed to the redirect_url parameter
    """
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        current_user = request.user
        current_user_id = request.user.id
        current_user_role_id = request.user.role.id
        current_user_role = request.user.role
        menus = MenuMaster.objects.filter(usrole = current_user_role_id)
        for chk in menus:
            if not chk.Is_Create:
                messages.info(request, "You are not authorize for this action.")
                return view_func(request,*args, **kwargs)
        messages.info(request, "You need to be logged out")
        print("You need to be logged out")
        return redirect(redirect_url)
    return wrapper 


def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.role.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper
    return decorators



def has_permission(self, request, view):
        if request.user.role.exists():
            
            return True
        else:
            return request.user.profile_limitation.can_create_project
