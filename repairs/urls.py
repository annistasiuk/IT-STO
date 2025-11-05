from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.repair_list_view, name='repair_list'),

]
