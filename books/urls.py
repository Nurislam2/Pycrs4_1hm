from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.book_list_view,name='book_list'),
    path('book_detail/<int:id>/', views.book_detail_view, name='book_detail'),
    path('about-me/', views.about_me),
    path('about-friend/', views.about_friend),
    path('current-time/', views.current_time),
]
