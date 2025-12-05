from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
    path('repairs/', include('repairs.urls')),
    path('billing/', include('billing.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]