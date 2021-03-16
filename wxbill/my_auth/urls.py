from django.urls import path
from . import views

app_name = 'my_auth'

urlpatterns = [
    path('', views.to_index, name='to_index'),
    path('page_login', views.page_login, name='page_login'),
    path('login_real', views.login_real, name='login_real'),
    path('to_test', views.to_test, name='to_test'),
]
