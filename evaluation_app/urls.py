from django.urls import path, include
from .views import NewUserRegistrationView
from rest_framework.routers import DefaultRouter
from .views import ProjectViewCRUD


router = DefaultRouter()
router.register(r'projects', ProjectViewCRUD, basename='comapanyprojects')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', NewUserRegistrationView.as_view(), name='new_user_register'),
    
]
