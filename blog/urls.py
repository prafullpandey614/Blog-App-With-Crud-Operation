from unicodedata import name
from django.urls import path ,include
from . import views
urlpatterns = [
    path("", views.StartingPageView.as_view(), name = "starting-page"),
    path("posts/", views.AllPostsView.as_view(),name="posts-page" ),
    # path("comment/handle", views.comment_handle),
    path("path/<slug:slug>", views.SinglePostView.as_view() ,name="post-detail-page"),
    path("read-later", views.ReadlaterView.as_view(), name="read-later")
    # path("/posts/<slug:slug>", views.posts, name ="post-detail-page")
]
