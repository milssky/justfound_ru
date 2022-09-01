from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from martor.models import MartorField

from telegram_group_poster.utils import send_message

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
    is_posted = models.BooleanField(default=False, blank=False, null=False)

    def make_full_markdown_post(self):
        return settings.POST_TEMPLATE.format(self.title, self.text, settings.SITE_HOST, self.get_absolute_url())

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('web_board:post_detail', kwargs={'post_id': self.pk})

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save()
        if not self.is_posted:
            self.is_posted = True
            send_message(self.make_full_markdown_post())


    class Meta:
        get_latest_by = ("pub_date",)
        ordering = ("-pub_date",)
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f"{self.title} at {self.pub_date}"
