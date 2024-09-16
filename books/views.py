from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models


def book_detail_view(request, id):
    if request.method == "GET":
        book = get_object_or_404(models.Books, id=id)
        return render(
            request,
            template_name='book_detail.html',
            context={
                'book': book
            }
        )



def book_list_view(request):
    if request.method == "GET":
        book_object = models.Books.objects.all()
        return render(
            request,
            template_name='book_list.html',
            context={
                'book_object': book_object
            })



def about_me(request):
    return HttpResponse("Это про меня Нурислам")


def about_friend(request):
    return HttpResponse("Это про моего друга Эрназар")


def current_time(request):
    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Текущее время: {time}")
