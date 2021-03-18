from django.urls import path
from . import views

app_name = 'charts'

urlpatterns = [
    path('', views.to_index, name='to_index'),
    path('get_today_bar_chart', views.get_today_bar_chart, name='get_today_bar_chart'),
    path('get_today_pie_chart', views.get_today_pie_chart, name='get_today_pie_chart'),
]