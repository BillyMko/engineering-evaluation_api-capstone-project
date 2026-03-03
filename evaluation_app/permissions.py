from rest_framework.permissions import BasePermission

class IsUserCompany(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user.is_authenticated and request.user.role == "company"
        return True
    
class IsProjectOwnerIfNotReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        return obj.created_by == request.user
    
class IsStudentThenSubmit(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role == "company":
                return False
        
        if request.method == "POST":
            return request.user.is_authenticated and request.user.role == "student"
        return True

class IsSubmissionTheOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        return obj.student == request.user


class IsCompanyThenEvaluate(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user.is_authenticated and request.user.role == "company"
        return True
    
class IsProjectOwnerThenEvaluate(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        return obj.submission.project.created_by == request.user

