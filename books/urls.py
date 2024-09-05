from django.urls import path
from . import views

urlpatterns = [
    path('about-me/', views.about_me),
    path('about-friend/', views.about_friend),
    path('current-time/', views.current_time),
]
