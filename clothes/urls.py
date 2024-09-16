from django.urls import path
from . import views

urlpatterns = [
    path('filter_clothes/', views.clothes_filter_view),

]
