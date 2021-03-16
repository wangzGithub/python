from django.contrib.auth.backends import AllowAllUsersModelBackend
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render, redirect
import urllib.parse, urllib.request
from .models import *
import json


class WxBackend(AllowAllUsersModelBackend):
    """
    通过微信授权认证
    """
    def authenticate(self, request, code=None):
        if code:
            params = {
                'appid': settings.WXAPPID,
                'secret': settings.WXSECRET,
                'code': code,
                'grant_type': 'authorization_code'
            }
            url = "https://api.weixin.qq.com/sns/oauth2/access_token?" \
                  + urllib.parse.urlencode(params).encode('utf-8').decode()
            data = json.loads(urllib.request.urlopen(url).read().decode('UTF-8'))
            access_token = data['access_token']
            if access_token:
                params = {
                    'access_token': access_token,
                    'openid': data['openid'],
                    'lang': 'zh_CN'
                }
                url = "https://api.weixin.qq.com/sns/userinfo?" + urllib.parse.urlencode(params).encode('utf-8').decode()
                data = json.loads(urllib.request.urlopen(url).read().decode('UTF-8'))
                if data['openid']:
                    user = User.objects.filter(wx__openid=data['openid'])
                    if user.count() > 0:
                        user = user[0]
                        wxprofile = user.wx
                    else:
                        user = User(username=data['openid'])
                        user.save()
                        wxprofile = WxProfile(user=user)
                    for item in data:
                        setattr(wxprofile, item, data[item])
                    wxprofile.save()
                    return user
        return None
