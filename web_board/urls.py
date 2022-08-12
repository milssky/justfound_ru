from django.urls import path

from .views import index, home, tg_login, send


urlpatterns = [
    path("", index),
    path("send/", send),
    path("tg_login/", tg_login),
    path("home/", home)
]
