from django.urls import path
from.import views
urlpatterns =[
    path('',views.index),
    path('about', views.about),
    path('gallery',views.gallery),
    path('contact',views.contact),
    path('service',views.service),
    path('single',views.single),
    path('login',views.login),
    path('register',views.register),
    path('driver',views.driver),
    path('hotel',views.hotel),
    path('tourpackages',views.tourpackages),
    path('home',views.home),
]