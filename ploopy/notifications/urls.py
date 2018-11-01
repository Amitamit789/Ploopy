from django.urls import path, include, re_path

from . import views

app_name = "notifications"
urlpatterns = [
    path("", view=views.Notifications.as_view(), name="notifications"),
    # re_path(r"(?P<image_id>[0-9]+)/like/", view=views.LikeImage.as_view(), name="like_image"),
    # path("<int:image_id>/like/", view=views.LikeImage.as_view(), name="like_image"),
]


