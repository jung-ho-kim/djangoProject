from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('home',views.Home),
    path('signin', views.login, name='main_login'),
    path('join', views.join, name='main_join'),
    path('logout', views.logout)
]
