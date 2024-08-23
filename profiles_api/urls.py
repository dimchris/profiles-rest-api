from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter

from profiles_api.views import HelloViewSet

from . import views


router = DefaultRouter()
router.register("hello-viewset", HelloViewSet, base_name="Hello View Set")

urlpatterns = [
    path("hello-view", views.HelloApiView.as_view()),
    path("", include(router.urls)),
]
