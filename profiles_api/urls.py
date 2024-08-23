from django.urls.conf import path
from . import views

urlpatterns = [
        path('hello-view', views.HelloApiView.as_view())
    ]
