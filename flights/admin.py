from django.contrib import admin
from .models import Flights, Airport, Passenger

# Register your models here.
class flightAdmin(admin.ModelAdmin):
    list_display = ('id', 'origin', 'destination', 'duration')

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ('flights', )

admin.site.register(Airport)
admin.site.register(Flights, flightAdmin)
admin.site.register(Passenger, PassengerAdmin)