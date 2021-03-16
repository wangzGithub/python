from django.db import models
from my_auth.models import User


# 账单分类表
class PayType(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50, verbose_name='分类名称', null=False)
    parent_pay_type = models.ForeignKey(to='self', verbose_name='上级分类', related_name='p_pay_type',
                                        on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(verbose_name='状态', default=1)
    user = models.ForeignKey(User, related_name='pt_user', on_delete=models.CASCADE, verbose_name='关联用户', null=False)
