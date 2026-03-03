from django.shortcuts import render
from rest_framework import generics
from .serializers import NewUserRegistrationSerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Project, Submission, Evaluation
from .serializers import ProjectSerializer, SubmissionSerializer, EvaluationSerializer
from .permissions import IsUserCompany,  IsProjectOwnerIfNotReadOnly, IsStudentThenSubmit, IsSubmissionTheOwner, IsCompanyThenEvaluate, IsProjectOwnerThenEvaluate
from rest_framework.permissions import IsAuthenticatedOrReadOnly

User = get_user_model()

class NewUserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = NewUserRegistrationSerializer



class ProjectViewCRUD(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [ IsUserCompany, IsProjectOwnerIfNotReadOnly, IsAuthenticatedOrReadOnly]

class SubmissionViewCRUD(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsStudentThenSubmit, IsSubmissionTheOwner, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role == "student":
                return Submission.objects.filter(student=user)

class EvaluationViewCRUD(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    permission_classes = [IsCompanyThenEvaluate, IsProjectOwnerThenEvaluate]

    def get_queryset(self):

        loggeduser = self.request.user
        if loggeduser.is_authenticated:
            if loggeduser.role == "student":
                return Evaluation.objects.filter(submission__student=loggeduser)
        
            elif loggeduser.role == "company":
                return Evaluation.objects.filter(submission__project__created_by=loggeduser)
        
        return Evaluation.objects.none()