from django.http.request import HttpRequest
from rest_framework.permissions import BasePermission, SAFE_METHODS


class UpdateOwnProfile(BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request: HttpRequest, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in SAFE_METHODS:
            return True

        return obj.id == request.user.id
