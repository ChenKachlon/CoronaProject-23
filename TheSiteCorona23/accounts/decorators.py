from django.shortcuts import redirect
from django.http import HttpResponse
from . import models
from django.shortcuts import get_object_or_404



def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator


def manger_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'manger' or group == 'help_desk':
            return view_func(request, *args, **kwargs)
        else:
            user = str(models.User.objects.get(id=request.user.id).last_name)
            url = 'department/' + user
            return redirect(url)
    return wrapper_func
