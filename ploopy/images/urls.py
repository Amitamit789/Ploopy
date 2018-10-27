from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    path("all/", view=views.ListAllImages.as_view(), name="all_images"),
    path("comments/", view=views.ListAllComments.as_view(), name="all_commnets"),
    path("likes/", view=views.ListAllLikes.as_view(), name="all_likes"),
]


