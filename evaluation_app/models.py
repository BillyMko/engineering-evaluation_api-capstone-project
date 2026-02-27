from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):

    ROLE_CHOICES = (('student', 'Student'),('company', 'Company'),)

    role = models.CharField(max_length=30, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"

class Project(models.Model):
    PROJECT_AVAILABILITY_CHOICES = (
        ('open', 'Open'),
        ('closed', 'Closed'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=PROJECT_AVAILABILITY_CHOICES, default='Open')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,limit_choices_to={'role': 'Company'},related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Submission(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='submission')
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'Student'},
        related_name='submission')

    solution = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.project.title}"

class Evaluation(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE,related_name='evaluation')
    solution_score = models.IntegerField()
    feedback = models.TextField()
    evaluated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"This evaluation is for {self.submission}"
