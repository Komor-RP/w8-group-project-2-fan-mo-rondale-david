from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Only post authors can delete their posts
    """

    def has_object_permission(self, request, view, question):
        if request.method in permissions.SAFE_METHODS:
            return True

        return question.author == request.user


class IsStarOwnerOrReadOnly(permissions.BasePermission):
    """
    Only original star owners can remove the star
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user