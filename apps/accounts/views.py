from django.shortcuts import render
from .serializers import RiderRegisterSerializer,DriverRegisterSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
User = get_user_model()

@api_view(['POST'])
def login(request):
    username = request.data.get("username").strip()
    password = request.data.get("password").strip()

    if not username or not password:
        return Response(
            {"error": "Username and password required"
             }, status=400)
    try:
        user = User.objects.get(username=username)


    except User.DoesNotExist:
        return Response({"error": "Invalid username or password"}, status=400)
    
    # check password
    if not check_password(password, user.password):
        return Response({"error": "Incorrect password"}, status=400)
    # create JWT tokens
    refresh = RefreshToken.for_user(user)
    access = refresh.access_token
    return Response({
            "message": "Login successful",
            "access_token": str(access),
            "refresh_token": str(refresh),
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }, status=200)
    
        


@api_view(["POST"])
def register_rider(request):
    serializer = RiderRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    return Response(serializer.errors,status=400)



