from django.urls import path

from .views import index, send


urlpatterns = [
    path("", index),
    path("send/", send)
]
