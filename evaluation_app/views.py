from django.shortcuts import render
from rest_framework import generics
from .serializers import NewUserRegistrationSerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Project, Submission
from .serializers import ProjectSerializer, SubmissionSerializer


User = get_user_model()

class NewUserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = NewUserRegistrationSerializer



class ProjectViewCRUD(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class SubmissionViewCRUD(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
