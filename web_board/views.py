from django.shortcuts import HttpResponse, render

from telegram_group_poster.utils import send_message


def index(request):
    return render(request, "base.html")


def send(request):
    send_message("Сообщение, отправленное с сайта")
    return HttpResponse("Отправлено")
