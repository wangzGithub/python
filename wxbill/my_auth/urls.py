from django.urls import path
from . import views

app_name = 'my_auth'

urlpatterns = [
    path('', views.to_index, name='to_index'),
    path('login_real', views.login_real, name='login_real'),
    path('to_test', views.to_test, name='to_test'),
    path('register', views.register, name='register'),
    path('to_resigter', views.to_register, name='to_register'),
]
