from django.shortcuts import render
from rest_framework import generics
from .serializers import NewUserRegistrationSerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer


User = get_user_model()

class NewUserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = NewUserRegistrationSerializer



class ProjectViewCRUD(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
