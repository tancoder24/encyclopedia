from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title_name>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("new", views.new, name = "new"),
    path("edit/<str:title_edit>", views.edit, name="edit"),
    path("random", views.random, name="random"),
]
