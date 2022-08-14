from django.contrib.auth import get_user_model
from django.db import models
from martor.models import MartorField

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = MartorField()
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор"
    )

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f"{self.title}"
