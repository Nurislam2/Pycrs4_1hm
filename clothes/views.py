from django.shortcuts import render

from . import models


# Create your views here.

def clothes_filter_view(request):
    if request.method == 'GET':
        clothes_child = models.Cloth.objects.filter(tags__name='для детей').order_by('-id')
        clothes_old = models.Cloth.objects.filter(tags__name='для пенсионеров').order_by('-id')
        clothes_adult = models.Cloth.objects.filter(tags__name='для взрослых').order_by('-id')
        return render(
            request,
            template_name='clothes_filter_list.html',
            context={
                'clothes_child': clothes_child,
                'clothes_old': clothes_old,
                'clothes_adult': clothes_adult
            }
        )