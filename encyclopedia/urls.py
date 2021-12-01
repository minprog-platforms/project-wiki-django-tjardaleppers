import random
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="title"),
    path("newpage", views.newpage, name="newpage"),
    path("search", views.search, name="search")
]
