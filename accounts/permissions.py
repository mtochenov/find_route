from rest_framework.permissions import BasePermissionMetaclass


class BasePermission(metaclass=BasePermissionMetaclass):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return True


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class AllowAny(BasePermission):
    def has_permission(self, request, view):
        return True
