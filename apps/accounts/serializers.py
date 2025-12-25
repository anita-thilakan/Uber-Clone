
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Rider, Driver

class RiderRegisterSerializer(serializers.ModelSerializer):

    #custom fields
    phone = serializers.CharField(write_only = True)
    payment_method = serializers.CharField(write_only = True)
    default_pick_up = serializers.CharField(write_only = True)
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ['username', 'email','password', 'phone','payment_method','default_pick_up',
                  ]
    
    def create(self,validated_data):

        # Extract Rider-specific fields and remove them from validated_data
        payment_method = validated_data.pop('payment_method')
        default_pick_up = validated_data.pop('default_pick_up')
        phone = validated_data.pop('phone')

        # Remaining data is safe for the User model
        user = User.objects.create_user(**validated_data)

        # Then create the Rider linked to that user
        Rider.objects.create(
            user=user,
            phone=phone,
            payment_method=payment_method,
            default_pick_up =default_pick_up
            )

        return user


class DriverRegisterSerializer(serializers.ModelSerializer):

    #custom fields
    phone = serializers.CharField(write_only= True)
    license = serializers.CharField(write_only= True)
    vehicle_model = serializers.CharField(write_only= True)
    vehicle_no = serializers.CharField(write_only= True)
    is_available = serializers.CharField(write_only= True)
    current_latitude = serializers.FloatField(write_only= True)
    current_longitude = serializers.FloatField(write_only= True)
    driver_photo = serializers.ImageField(write_only= True)
    password = serializers.CharField(write_only= True)

    class Meta:
        model= User
        fields = ['username','email','password','phone','license','vehicle_model',
                  'vehicle_no','is_available','current_latitude','current_longitude',
                  'driver_photo','password']
        
    def create(self, validated_data):
        #pop fields from User
        phone = validated_data.pop('phone')
        license = validated_data.pop('license')
        vehicle_model = validated_data.pop('vehicle_model')
        vehicle_no = validated_data.pop('vehicle_no')
        is_available = validated_data.pop('is_available')
        current_latitude = validated_data.pop('current_latitude')
        current_longitude = validated_data.pop('current_longitude')
        driver_photo = validated_data.pop('driver_photo')
        
        #create user profile
        user = User.objects.create_user(**validated_data)

         # Then create the Driver linked to that user
        Driver.objects.create(
            user=user,
            phone = phone,
            license = license,
            vehicle_model = vehicle_model,
            vehicle_no = vehicle_no,
            is_available = is_available,
            current_latitude = current_latitude,
            current_longitude = current_longitude,
            driver_photo = driver_photo
            
            )

        return user




 

