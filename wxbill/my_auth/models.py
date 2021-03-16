from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class WxProfile(models.Model):
    def __str__(self):
        return self.nickname
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户', related_name='wx')
    openid = models.CharField(max_length=50, verbose_name='OpenId')
    nickname = models.CharField(max_length=100, verbose_name='昵称', null=True)
    sex = models.CharField(max_length=1, verbose_name='性别', null=True)
    province = models.CharField(max_length=20, verbose_name='省份', null=True)
    city = models.CharField(max_length=20, verbose_name='城市', null=True)
    country = models.CharField(max_length=50, verbose_name='国家', null=True)
    headimgurl = models.URLField(null=True, verbose_name='头像链接')
    unionid = models.CharField(max_length=50, verbose_name='UnionId')
