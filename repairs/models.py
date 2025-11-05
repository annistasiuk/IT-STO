from django.db import models
from cars.models import Car

class Repair(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новий'),
        ('in_progress', 'В роботі'),
        ('awaiting_parts', 'Очікує запчастин'),
        ('completed', 'Завершено'),
    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='repairs')
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Ремонт для {self.car.make} ({self.status})"