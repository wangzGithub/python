from .models import PayType


# 获取登录用户关联的一级支出分类
def get_p_pay_type_list(request):
    p_pay_type = PayType.objects.filter(user_id=request.user.id, p_pay_type=None, status=1)
    p_pay_type_list = []
    for pay_type in p_pay_type:
        item = {}
        item.update({
            'id': pay_type.id, 'name': pay_type.name
        })
        p_pay_type_list.append(item)
    return p_pay_type_list


# 保存支出类型
def save_pay_type(request):
    name = request.POST.get('name')
    p_id = request.POST.get('p_id')
    result = {}
    has_pay_type = PayType.objects.filter(name=name)
    if len(has_pay_type) > 0:
        result.update({
            'code': 2, 'msg': 'name exist'
        })
    else:
        if p_id == '0':
            p_pay_type = None
        else:
            p_pay_type = PayType.objects.get(id=p_id)
        try:
            pay_type = PayType(name=name, parent_pay_type=p_pay_type, status=1, user_id=request.user.id)
            pay_type.save()
            result.update({
                'code': 0, 'msg': 'success'
            })
        except:
            result.update({
                'code': 1, 'msg': 'failed'
            })
    return result
