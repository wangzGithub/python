from django.urls import path
from . import views

app_name = 'charts'

urlpatterns = [
    path('', views.to_index, name='to_index'),
]