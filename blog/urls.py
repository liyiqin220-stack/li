from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('article/', views.article, name='article'),
    path('guestbook/', views.guestbook, name='guestbook'),
]
