from django.urls import path
from . import views

app_name = 'bill'

urlpatterns = [
    path('', views.to_index, name='to_index'),
    path('to_add_bill', views.to_add_bill, name='to_add_bill'),
]
