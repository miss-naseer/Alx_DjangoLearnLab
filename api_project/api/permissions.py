from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Safe methods = GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only admin users can modify
        return request.user and request.user.is_staff
