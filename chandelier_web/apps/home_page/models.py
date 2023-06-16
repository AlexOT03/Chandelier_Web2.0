from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)
    affair = models.CharField(max_length=200)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"Mensaje of {self.name} - {self.affair}"