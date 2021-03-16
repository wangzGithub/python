from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
import urllib.parse
from django.urls import reverse
from django.http import HttpResponse


# 项目入口， 微信授权后进入项目
def to_index(request):
    return render(request, 'my_auth/index.html', {})


def page_login(request):
    params = {
        'appid': settings.WXAPPID,
        'redirect_uri': 'http://127.0.0.1:8000/my_auth/login_real',
        'response_type': 'code',
        'scope': 'snsapi_userinfo'
    }
    url = "https://open.weixin.qq.com/connect/oauth2/authorize?" \
          + urllib.parse.urlencode(params).encode('utf-8').decode() + "#wechat_redirect"
    return redirect(url)


def login_real(request):
    code = request.GET.get('code')
    if code:
        user = authenticate(request, code=code)
        if user is not None:
            login(request, user)
            return redirect(reverse('charts:to_index'))
        return HttpResponse("登录失败")


def my_logout(request):
    logout(request)
    return render(request, 'my_auth/index.html', {})


def to_test(request):
    return render(request, 'my_auth/test.html', {})
