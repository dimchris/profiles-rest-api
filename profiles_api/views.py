from django.http.request import HttpRequest
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet

from profiles_api.models import ProfileFeedItem, UserProfile
from profiles_api.permissions import UpdateOwnProfile, UpdateOwnStatus
from profiles_api.serializers import (
    HelloSerializer,
    ProfileFeedItemSerializer,
    UserProfileSerializer,
)


class UserProfileFeedViewSet(ModelViewSet):
    """Handlers creating and updating feeding items"""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, UpdateOwnStatus)
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileViewSet(ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (SearchFilter,)
    search_fields = ("name", "email")


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = HelloSerializer

    def get(self, request: HttpRequest, format=None) -> Response:
        """Returns a list of APIView features"""
        an_apiview = [
            "          Uses HTTP methods",
            "Similar to django view",
            "most control",
            "maps manually to url",
        ]
        return Response(
            {
                "message": "Hello",
                "an_apivie": an_apiview,
            }
        )

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response(message)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk=None):
        """Handling updating an object"""
        return Response(
            {
                "method": "PUT",
            }
        )

    def patch(self, request, pk=None):
        """Handling a partial update of an object"""
        return Response(
            {
                "method": "PATCH",
            }
        )

    def delete(self, request, pk=None):
        """Handling a deletion of an object"""
        return Response(
            {
                "method": "DELETE",
            }
        )


class HelloViewSet(ViewSet):
    """Test API view set"""

    serializer_class = HelloSerializer

    def list(self, request):
        """Return a hello message"""
        an_apiview = [
            "Uses HTTP methods",
            "Similar to django view",
            "most control",
            "maps manually to url",
        ]
        return Response(
            {
                "message": "Hello",
                "an_apivie": an_apiview,
            }
        )

    def create(self, request):
        """Create a new Hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response(
                {
                    "message": message,
                }
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""
        return Response(
            {
                "http_method": "GET",
            }
        )

    def update(self, request, pk=None):
        """Handle updating an object by its id"""
        return Response(
            {
                "http_method": "PUT",
            }
        )

    def partial_update(self, request, pk=None):
        """Handle partial updating an object by its id"""
        return Response(
            {
                "http_method": "PATCH",
            }
        )

    def destroy(self, request, pk=None):
        """Handle removing an object by its id"""
        return Response(
            {
                "http_method": "DELETE",
            }
        )
