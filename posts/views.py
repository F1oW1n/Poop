from django.shortcuts import render
from posts.models import Post
from django.views.generic import ListView


class PostListview(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'all_posts'
    ordering = '-date'

