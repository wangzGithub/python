from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import urllib.parse
from django.urls import reverse
from django.http import HttpResponse
import json


# 项目入口， 微信授权后进入项目
def to_index(request):
    return render(request, 'my_auth/index.html', {})


# register
def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    password = make_password(password)
    _user = User.objects.filter(username=username)
    result = {}
    if len(_user) > 0:
        result.update({
            'code': 1, 'msg': 'username is exist'
        })
    else:
        user = User(username=username, password=password)
        user.save()
        result.update({
            'code': 0, 'msg': 'success'
        })
    return HttpResponse(json.dumps(result), content_type='application/json')


# login
def login_real(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    result = {}
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        result.update({
            'code': 0, 'msg': 'success'
        })
    else:
        result.update({
            'code': 1, 'msg': 'failed'
        })
    return HttpResponse(json.dumps(result), content_type='application/json')


def my_logout(request):
    logout(request)
    return render(request, 'my_auth/index.html', {})


def to_register(request):
    return render(request, 'my_auth/register.html', {})


def to_test(request):
    return render(request, 'my_auth/test.html', {})
