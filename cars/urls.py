from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_car_view, name='add_car'),
    path('list/', views.car_list_view, name='car_list'),
]