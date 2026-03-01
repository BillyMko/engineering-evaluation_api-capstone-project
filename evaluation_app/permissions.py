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