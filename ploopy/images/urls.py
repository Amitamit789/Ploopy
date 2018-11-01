from django.urls import path, include, re_path

from . import views

app_name = "images"
urlpatterns = [
    path("", view=views.Feed.as_view(), name="feed"),
    path("<int:image_id>/", view=views.ImageDetail.as_view(), name="feed"),
    # re_path(r"(?P<image_id>[0-9]+)/like/", view=views.LikeImage.as_view(), name="like_image"),
    path("<int:image_id>/likes/", view=views.LikeImage.as_view(), name="like_image"),
    path("<int:image_id>/unlikes/", view=views.UnLikeImage.as_view(), name="like_image"),
    path("<int:image_id>/comments/", view=views.CommentOnImage.as_view(), name="comment_image"),
    path("comments/<int:comment_id>/", view=views.Comment.as_view(), name="comment"),
    path("search/", view=views.Search.as_view(), name="search"),
    path("<int:image_id>/comments/<int:comment_id>/", view=views.ModerateComments.as_view(), name="comment_image"),
]


