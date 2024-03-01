from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("send_content", views.send_content, name="send_content"),
    path("edit_content", views.edit_content, name="edit_content"),
    path("delete_content", views.delete_content, name="delete_content"),
    path("get_content", views.get_content, name="get_content"),
    path("get_all_contents", views.get_all_contents, name="get_contents")
]