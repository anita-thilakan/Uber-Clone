from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#create rider and driver models


class Rider(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length= 15)
    payment_method = models.CharField(max_length= 30)
    default_pick_up = models.TextField()
    

    def __str__(self):
        return self.user.username
    

class Driver(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length= 15)
    vehicle_type = models.CharField(max_length= 20)
    created_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.user.username
