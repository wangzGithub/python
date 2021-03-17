from django.db import models
from pay_type.models import PayType
from my_auth.models import User


# 账单表
class Bill(models.Model):
    id = models.IntegerField(verbose_name='primary key', primary_key=True)
    name = models.CharField(max_length=50, verbose_name='名称', null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='金额', null=False)
    pay_type = models.ForeignKey(PayType, related_name='pay_type', on_delete=models.SET_NULL,
                                 verbose_name='关联类型', null=True)
    bill_date = models.DateField(verbose_name='记录日期', null=False, db_index=True)
    year = models.IntegerField(verbose_name='年', db_index=True)
    month = models.IntegerField(verbose_name='月', db_index=True)
    day = models.IntegerField(verbose_name='日', db_index=True)
    description = models.CharField(max_length=250, verbose_name='说明', null=True)
    user = models.ForeignKey(User, related_name='bill_user', on_delete=models.CASCADE, verbose_name='关联用户', null=True)
