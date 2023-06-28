from django.db import models
from chandelier_web.apps.admin_page_states.models import State
from chandelier_web.apps.admin_page_themes.models import Theme

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    location_length = models.CharField(max_length=200, blank=True, null=True)
    location_width = models.CharField(max_length=200, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    web_site = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    parking = models.BooleanField(default=False)

    def __str__(self):
        return self.name
      
class Image(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='location_images', blank=True, null=True)

    def __str__(self):
        return str(self.image)

class OpeningHour(models.Model):
    WEEKDAYS = (
        (1, 'Lunes'),
        (2, 'Martes'),
        (3, 'Miércoles'),
        (4, 'Jueves'),
        (5, 'Viernes'),
        (6, 'Sábado'),
        (7, 'Domingo'),
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='opening_hours')
    day_of_week = models.IntegerField(choices=WEEKDAYS, blank=True, null=True)
    opening_time = models.TimeField(blank=True, null=True)
    closing_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.day_of_week

# class Location(models.Model):
#     name = models.CharField(max_length=100)
#     owner = models.CharField(max_length=100)
#     location = models.CharField(max_length=200)
#     location_length = models.CharField(max_length=200, blank=True, default=0)
#     location_width = models.CharField(max_length=200, blank=True, default=0)
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
#     capacity = models.IntegerField()
#     created_date= models.DateField(auto_now_add=True)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     description = models.TextField(blank=True)
#     images = models.ImageField(upload_to="imagenes")
    
#     def __str__(self):
#       return self.name

# class OpeningHour(models.Model):
#     location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='opening_hours')
#     day_of_week = models.IntegerField(choices=((1, 'Lunes'), (2, 'Martes'), (3, 'Miércoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sábado'), (7, 'Domingo')))
#     opening_time = models.TimeField()
#     closing_time = models.TimeField()
    
#     def __str__(self):
#       return self.location