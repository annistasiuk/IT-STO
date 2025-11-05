from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    vin = models.CharField(max_length=17, unique=True)
    owner_name = models.CharField(max_length=200)
    owner_phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.make} {self.model} ({self.vin})"
