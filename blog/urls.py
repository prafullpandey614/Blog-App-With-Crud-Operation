from unicodedata import name
from django.urls import path ,include
from . import views
urlpatterns = [
    path("", views.StartingPageView.as_view(), name = "starting-page"),
    path("posts/", views.posts ,name="posts-page" ),
    # path("comment/handle", views.comment_handle),
    path("path/<slug:slug>", views.post_detail ,name="post-detail-page"),
    # path("/posts/<slug:slug>", views.posts, name ="post-detail-page")
]
