from rest_framework import permissions


class IsModer(permissions.BasePermission):
    message = 'Adding customers not allowed.'
    """Проверка на модератора."""

    def has_permission(self, request, view):
        return request.user.groups.filter(mane="moders").exists()


class IsOwner(permissions.BasePermission):
    """Проверка на владельца или только чтение."""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
