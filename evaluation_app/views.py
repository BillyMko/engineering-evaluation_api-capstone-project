from django.shortcuts import render
from rest_framework import generics
from .serializers import NewUserRegistrationSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class NewUserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = NewUserRegistrationSerializer

