from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

class CurrentUserOrAdmin(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        STAFF_NOT_ALLOWED = ['PUT','DELETE','PATCH']
        user = request.user
        if request.method in STAFF_NOT_ALLOWED:
            return user.is_superuser
        return user.is_superuser or user.is_staff
    
    def has_permission(self, request, view):
        if request.method == "GET":
            print("hello")
            return True
        return bool(request.user.is_staff and request.user.is_authenticated)

