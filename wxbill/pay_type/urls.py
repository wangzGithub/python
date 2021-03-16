from django.urls import path
from . import views

app_name = 'pay_type'

urlpatterns = [
    path('to_list', views.to_list, name='to_list'),
    path('to_add_pay_type', views.to_add_pay_type, name='to_add_pay_type'),
    path('get_p_pay_type_list', views.get_p_pay_type_list, name='get_p_pay_type_list'),
    path('save_pay_type', views.save_pay_type, name='save_pay_type'),
]