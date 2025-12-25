from django.contrib import admin
from .models import DriverLocation,RideDetails
# Register your models here.
admin.site.register(RideDetails)
admin.site.register(DriverLocation)

