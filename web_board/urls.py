from django.urls import path

from .views import index, history, home, tg_login, send


app_name="web_board"

urlpatterns = [
    path("", index),
    path("history/", history, name="history"),
    path("send/", send),
    path("tg_login/", tg_login),
    path("home/", home)
]
