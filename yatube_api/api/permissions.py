from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request but other
        # only to the owner
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
