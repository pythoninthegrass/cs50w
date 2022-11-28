#!/usr/bin/env python3

from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.get_entries, name="search"),
    path("create", views.create, name="create"),
    path("random", views.random_entry, name="random"),
]
