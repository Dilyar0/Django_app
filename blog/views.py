from django.shortcuts import render
from django.http import HttpResponse
from . import models

def hello_world(request):
    return HttpResponse("<p>Hello World by TELIDAS<p>")


def post_all(request):
    post = models.Post.objects.all()
    return render(request, "post_list.html", {"post": post})