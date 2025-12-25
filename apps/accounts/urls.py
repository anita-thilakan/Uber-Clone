from django.urls import path
from . import views

urlpatterns = [
    path('register/rider',views.register_rider, name='registerrider'),
    # path('register/driver',views.register_driver, name='registerdriver')
    path('login',views.login,name='login')
]