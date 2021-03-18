from django.urls import path
from . import views

app_name = 'bill'

urlpatterns = [
    path('', views.to_index, name='to_index'),
    path('to_add_bill', views.to_add_bill, name='to_add_bill'),
    path('save_bill', views.save_bill, name='save_bill'),
    path('delete_bill', views.delete_bill, name='delete_bill'),
]
