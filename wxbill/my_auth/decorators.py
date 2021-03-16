from django.http import HttpResponse
from django.shortcuts import redirect, render


def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('my_auth:to_index')
    return wrapper_func


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('my_auth:to_index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
