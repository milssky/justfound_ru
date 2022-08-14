from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, HttpResponsePermanentRedirect, render

from users.utils import validate_auth_data
from telegram_group_poster.utils import send_message
from .models import Post


def index(request):
    posts = Post.objects.select_related("author")
    return render(request, "web_board/page.html", {"posts": posts})


@login_required
def send(request):
    send_message("Сообщение, отправленное с сайта")
    return HttpResponse("Отправлено")


def tg_login(request):
    auth_data = dict(request.GET.items())
    if not validate_auth_data(auth_data):
        return HttpResponse('Wrong auth data. Check it and try again')
    user = authenticate(username=auth_data['username'])
    login(request, user)
    return HttpResponsePermanentRedirect('/home')


@login_required
def home(request):
    return HttpResponse(f"{request.user} logged")
