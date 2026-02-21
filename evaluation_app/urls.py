from django.urls import path
from .views import NewUserRegistrationView

urlpatterns = [
    path('register/', NewUserRegistrationView.as_view(), name='new_user_register'),
]
