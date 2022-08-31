from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, HttpResponsePermanentRedirect, render, get_object_or_404

from users.utils import validate_auth_data
from telegram_group_poster.utils import send_message
from .models import Post


def index(request):
    post = Post.objects.select_related("author").latest()
    return render(request, "web_board/page.html", {"post": post})


def history(request):
    posts = Post.objects.select_related("author")
    post_dates = posts.values_list('pub_date')
    return render(
        request,
        "web_board/history.html",
        {'posts': posts}
    )


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "web_board/page.html", {"post": post})


@login_required
def send(request):
    send_message("Сообщение, **отправленное с сайта**")
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
