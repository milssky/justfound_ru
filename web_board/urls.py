from django.urls import path

from .views import index, history, post_detail, tg_login, ManifestView


app_name = "web_board"

urlpatterns = [
    path("", index, name="index"),
    path("history/", history, name="history"),
    path("history/<int:post_id>/", post_detail, name="post_detail"),
    path("tg_login/", tg_login),
    path("manifest/", ManifestView.as_view(), name="manifest")
]
