from django.db import models
# from django.contrib.gis.db import models as geomodels

from apps.accounts.models import Driver,Rider
# Create your models here.

class DriverLocation(models.Model):
    user = models.OneToOneField(Driver,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    latitude = models.DecimalField(max_digits=9,decimal_places=6)
    # location = models.PointField(srid=4326)  # Stores latitude & longitude as a Point
    longitude = models.DecimalField(max_digits=9,decimal_places=6)

    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}@{self.timestamp}"


class RideDetails(models.Model):
    rider  = models.OneToOneField(Rider,on_delete=models.CASCADE)
    driver = models.OneToOneField(Driver,on_delete=models.CASCADE)
    pick_up = models.CharField(max_length=20)
    drop = models.CharField(max_length=20)
    
    CHOICES = (
        ('allocated', 'Allocated'),
    ('complete', 'Complete'),
    )
    status = models.CharField(max_length=20,choices=CHOICES,default='allocated')
    fare = models.DecimalField(max_digits=5,decimal_places=2)