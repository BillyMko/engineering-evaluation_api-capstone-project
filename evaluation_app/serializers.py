from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import Project, Submission, Evaluation

User = get_user_model()

class NewUserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'role')


    def create(self, validated_data):
        newuser = User(username=validated_data['username'],first_name=validated_data['first_name'],last_name=validated_data['last_name'],email=validated_data['email'],role=validated_data['role'])
        newuser.set_password(validated_data['password'])
        newuser.save()
        return newuser





class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['id','title','description','status','created_by','created_at']
        read_only_fields = ['id', 'created_at']


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = [
            'id',
            'project',
            'student',
            'solution',
            'submitted_at'
        ]
        read_only_fields = ['id', 'student', 'submitted_at']

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = [
            'id',
            'submission',
            'solution_score',
            'feedback',
            'evaluated_at'
        ]
        read_only_fields = ['id', 'evaluated_at']
