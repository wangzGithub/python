from django.shortcuts import render
from . import utils
import time
from .models import Bill
from pay_type.models import PayType
from my_auth.decorators import *


# 账单首页 显示列表
@authenticated_user
def to_index(request):
    today = time.strftime('%Y-%m-%d', time.localtime())
    bill_list = Bill.objects.filter(bill_date=today, user_id=request.user.id)
    context = {}
    context.update({
        'bill_list': bill_list,
        'today': today
    })
    return render(request, 'bill/index.html', context)


# 跳转到添加账单页面
@authenticated_user
def to_add_bill(request):
    context = {}
    p_pay_type_list = PayType.objects.filter(user_id=request.user.id, parent_pay_type=None)
    context.update({
        'p_pay_type_list': p_pay_type_list
    })
    return render(request, 'bill/add_bill.html', context)
