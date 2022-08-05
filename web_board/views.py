from django.shortcuts import HttpResponse

from telegram_group_poster.utils import send_message


def index(request):
    return HttpResponse("Hello")


def send(request):
    send_message("Сообщение, отправленное с сайта")
    return HttpResponse("Отправлено")
