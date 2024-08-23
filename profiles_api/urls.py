from django.urls.conf import include, path
from rest_framework.routers import DefaultRouter

from profiles_api.views import HelloViewSet, UserProfileFeedViewSet, UserProfileViewSet

from . import views

router = DefaultRouter()
router.register("hello-viewset", HelloViewSet, base_name="Hello View Set")
router.register("profile", UserProfileViewSet)
router.register("feed", UserProfileFeedViewSet)

urlpatterns = [
    path("hello-view", views.HelloApiView.as_view()),
    path("login/", views.UserLoginApiView.as_view()),
    path("", include(router.urls)),
]
