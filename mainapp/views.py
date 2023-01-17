from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy
from .models import Post

# Create your views here.


class PostDisplayView(ListView):
    model = Post
    template_name = "home.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(CreateView):
    model = Post
    template_name = "post_create.html"
    fields = ["title", "author", "body"]


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"

    success_url = reverse_lazy("home")


class PostEditView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]
