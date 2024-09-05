from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def about_me(request):
    return HttpResponse("Это про меня Нурислам")


def about_friend(request):
    return HttpResponse("Это про моего друга Эрназар")


def current_time(request):
    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Текущее время: {time}")
