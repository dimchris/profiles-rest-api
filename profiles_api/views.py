from django.http.request import HttpRequest
from django.template.context_processors import request
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from profiles_api.serializers import HelloSerializer


# Create your views here.
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
