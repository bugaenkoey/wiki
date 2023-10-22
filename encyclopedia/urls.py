from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add",views.add,name="add"),
    path("search", views.search,name="search"),
    path("random_page",views.random_page, name="random_page"),
    path("create_new_page", views.create_new_page, name="create_new_page"),
    path("edit_page", views.edit_page, name="edit_page"),
    path("seve_edit",views.seve_edit, name="seve_edit"),
    path("<str:title>", views.get_entry, name="get_entry")
]
