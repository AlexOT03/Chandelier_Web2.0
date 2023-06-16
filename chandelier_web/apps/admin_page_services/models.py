from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=8, max_digits=8)
    duration = models.TimeField(blank=True)