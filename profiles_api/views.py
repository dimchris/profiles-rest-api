from django.http.request import HttpRequest
from django.template.context_processors import request
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class HelloApiView(APIView):
    """ Test API View"""

    def get(self, request: HttpRequest, format = None) -> Response:
        """ Returns a list of APIView features """
        an_apiview = [
            '          Uses HTTP methods',
                       'Similar to django view',
                       'most control',
                       'maps manually to url',
                    ]
        return Response({'message':'Hello', 'an_apivie': an_apiview})
