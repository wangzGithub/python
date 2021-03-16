from my_auth.decorators import *
from .models import PayType
from . import utils
import json


# 支出分类 列表页面
@authenticated_user
def to_list(request):
    context = {}
    pay_type_list = PayType.objects.filter(user_id=request.user.id, status=1, parent_pay_type=None)
    context.update({
        'pay_type_list': pay_type_list
    })
    return render(request, 'pay_type/list.html', context)


# 跳转到新增支出分类页面
@authenticated_user
def to_add_pay_type(request):
    return render(request, 'pay_type/add_pay_type.html', {})


# 获取登录用户关联的一级支出分类
@authenticated_user
def get_p_pay_type_list(request):
    p_pay_type_list = utils.get_p_pay_type_list(request)
    print(p_pay_type_list)
    return HttpResponse(json.dumps(p_pay_type_list), content_type='application/json')


# 保存支出类型
@authenticated_user
def save_pay_type(request):
    result = utils.save_pay_type(request)
    return HttpResponse(json.dumps(result), content_type='application/json')
