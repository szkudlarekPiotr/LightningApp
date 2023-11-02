from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.kwargs["pk"] == request.user.id:
            return True
        else:
            return request.method in permissions.SAFE_METHODS
