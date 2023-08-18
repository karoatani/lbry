from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

class CurrentUserOrAdmin(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return user.is_superuser or user.is_staff
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user.is_staff and request.user.is_authenticated)



class CurrentStaffOrAdmin(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return user.is_superuser
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user.is_superuser and request.user.is_authenticated)
    