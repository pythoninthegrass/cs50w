from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("create", views.create, name="create"),
    path("edit_list", views.edit_list, name="edit_list"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("search", views.get_entries, name="search"),
    path("create", views.create, name="create"),
    path("random", views.random_entry, name="random"),
]
