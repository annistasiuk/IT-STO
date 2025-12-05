from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.repair_list_view, name='repair_list'),
    path('add/', views.add_repair_view, name='add_repair'),
    path('<int:repair_id>/edit/', views.edit_repair_view, name='edit_repair'),
]
