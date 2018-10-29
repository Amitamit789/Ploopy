from django.urls import path, include, re_path

from . import views

app_name = "images"
urlpatterns = [
    path("", view=views.Feed.as_view(), name="feed"),
    # re_path(r"(?P<image_id>[0-9]+)/like/", view=views.LikeImage.as_view(), name="like_image"),
    path("<int:image_id>/like/", view=views.LikeImage.as_view(), name="like_image"),
    path("<int:image_id>/comment/", view=views.CommentOnImage.as_view(), name="comment_image"),
]


