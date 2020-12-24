from django.urls import include 
from django.contrib import admin
from django.urls import path
from DotaSite import views
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('Tournaments/', views.listtournament , name='listtournament'),
    path('Gamers/', views.listgamermmr , name='listgamermmr'),  
    path('Match/', views.listmatch , name='listmatch'),  
    path("register/", views.register, name="register")
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
