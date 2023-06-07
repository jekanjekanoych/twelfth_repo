from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_blog/", views.create_blog, name="create_blog"),
    path("get_blog/<int:id>", views.get_blog, name="get_blog"),
    path("get_blog/<int:id>/update", views.update, name="update_blog"),
]
