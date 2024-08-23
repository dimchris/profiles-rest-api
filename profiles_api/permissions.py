from django.http.request import HttpRequest
from rest_framework.permissions import SAFE_METHODS, BasePermission


class UpdateOwnProfile(BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request: HttpRequest, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(BasePermission):
    def has_object_permission(self, request, view, obj):
        """Check if update own status"""
        if request.method in SAFE_METHODS:
            return True

        return obj.id == request.user.id
