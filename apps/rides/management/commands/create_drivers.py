from django.core.management import BaseCommand
from apps.accounts.models import Driver,Rider
from apps.rides.models import DriverLocation
from django.contrib.auth.models import User
from datetime import timezone, datetime
import random
class Command(BaseCommand):
    help= "create drivers"

    def handle(self, *args, **options):
        #barkatulla location
        CENTRE_LAT = 23.20168964581568
        CENTRE_LNG = 77.45232947979531

        #delete all existing dummy users from User and Driver
        # bcoz of cascade inside models any user deleted from User auto deletes Driver and DriverLocation entry
        User.objects.filter(username__startswith='user_').delete()
        # Driver.objects.filter(username__startswith='user_').delete()
        # DriverLocation.objects.filter(username__startswith='user_').delete()
        print("all deleted from Users, Drivers, DriverLocation")
        for i in range(1,31):

            #around this place
            val = random.uniform(0.2,0.5)

            LAT = random.uniform(CENTRE_LAT - val, CENTRE_LAT + val)
            LNG = random.uniform(CENTRE_LNG - val, CENTRE_LNG + val)

            user = User.objects.create(
                username = f"user_{i}",
                email = f"user_{i}@gmail.com",
                
            )

            if user:

                #Driver
                driver = Driver.objects.create(
                    user = user,
                    phone = f"+91{random.randint(8785546223,9999999999)}",
                    vehicle_type = f"{random.choice(['SUV','SEDAN','PRIME'])}"

                )

                if driver:
                    # Driver Locations
                    driverloc =  DriverLocation.objects.create(
                        user = driver,
                        timestamp =  datetime.now(timezone.utc),
                        latitude = LAT,
                        longitude = LNG

                    )
                else:return
            else:return
        print(f" {i} user created")
