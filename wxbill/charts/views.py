from django.shortcuts import render
from my_auth.decorators import *
import time
from bill.models import Bill
import json
from django.db.models import Sum


@authenticated_user
def to_index(request):
    content = {}
    content.update({
        'username': request.user.username
    })
    return render(request, 'charts/index.html', context=content)


# 获取当日账单柱状图
def get_today_bar_chart(request):
    today = time.strftime('%Y-%m-%d', time.localtime())
    bill_list = Bill.objects.filter(user_id=request.user.id, bill_date=today)
    result = []
    if len(bill_list) > 0:
        for bill in bill_list:
            item = {'name': bill.name, 'price': float(bill.price)}
            result.append(item)
    return HttpResponse(json.dumps(result), content_type='application/json')


# 获取当日账单饼图
def get_today_pie_chart(request):
    today = time.strftime('%Y-%m-%d', time.localtime())
    list = Bill.objects.filter(user_id=request.user.id, bill_date=today) \
        .values('pay_type__name').annotate(total=Sum('price'))
    result = []
    if len(list) > 0:
        for param in list:
            item = {'name': param.get('pay_type__name'), 'price': float(param.get('total'))}
            result.append(item)
    print(result)
    return HttpResponse(json.dumps(result), content_type='application/json')
