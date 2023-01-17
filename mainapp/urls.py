from django.urls import path
from .views import (
    PostDisplayView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostEditView,
)

urlpatterns = [
    path("", PostDisplayView.as_view(), name="home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
    path("post/<int:pk>/edit", PostEditView.as_view(), name="post_edit"),
]
