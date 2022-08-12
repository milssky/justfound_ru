from django.contrib.auth.models import AbstractUser
from django.db import models


class TgUser(AbstractUser):
    tg_username = models.CharField(max_length=200)
    photo_url = models.URLField(default="")

    def __str__(self):
        return f"{self.username}:{self.tg_username}"
