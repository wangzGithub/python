from django.urls import path
from . import views

app_name = 'my_auth'

urlpatterns = [
    path('', views.to_index, name='to_index'),
    path('to_test', views.to_test, name='to_test'),
]
