import time
from .models import Bill
from datetime import datetime


# 保存账单
def save_bill(request):
    name = request.POST.get('name')
    bill_date = request.POST.get('bill_date')
    pay_type_id = request.POST.get('pay_type_id')
    price = request.POST.get('price')
    description = request.POST.get('description')
    year, month, day = bill_date.split('-')
    date = datetime(int(year), int(month), int(day))
    bill = Bill(name=name, bill_date=date, pay_type_id=pay_type_id, price=price,
                year=int(year), month=int(month), day=int(day),
                description=description, user_id=request.user.id)
    try:
        bill.save()
        result = {'code': 0, 'msg': 'save success'}
    except:
        result = {'code': 1, 'msg': 'save failed'}
    return result


# 删除账单
def delete_bill(request):
    bill_id = request.POST.get('id')
    result = {}
    print(bill_id)
    bill_list = Bill.objects.filter(id=bill_id)
    print(bill_list)
    if len(bill_list) > 0:
        bill = bill_list[0]
        try:
            bill.delete()
            result.update({
                'code': 0, 'msg': 'success'
            })
        except:
            result.update({
                'code': 1, 'msg': 'error'
            })
    else:
        result.update({
            'code': 2, 'msg': 'Bill not found'
        })
    return result
