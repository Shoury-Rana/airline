from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f'{self.city} ({self.code})'
    

class Flights(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.IntegerField()
    
    def __str__(self):
        return f'{self.id}: {self.origin} to {self.destination}'
    
class Passenger(models.Model):
    f_name = models.CharField(max_length=32)
    l_name = models.CharField(max_length=32)
    flights = models.ManyToManyField(Flights, blank=True, related_name='passenger')

    def __str__(self):
        return f'{self.f_name} {self.l_name}'