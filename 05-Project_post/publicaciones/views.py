from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

class PostListView(ListView):
    template_name = 'home.html'
    model = Post


class PostDetailView(DetailView):
    template_name = 'detail.html'
    model = Post


# CRUD
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    fields = ["title", "description", "image"]
    template_name = 'crud/create.html'
    success_url = reverse_lazy('home')


class PostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    fields = ["title", "description", "image"]
    template_name = 'crud/update.html'
    success_url = reverse_lazy('home')


class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('home')
