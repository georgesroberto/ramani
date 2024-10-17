from rest_framework import permissions

class IsEmployer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.profile.role == 'employer'


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.profile.role == 'employee'


class IsAdmin(permissions.BasePermission):
    """
    Custom permission to grant access to superusers (admin).
    """
    def has_permission(self, request, view):
        return request.user.is_superuser
