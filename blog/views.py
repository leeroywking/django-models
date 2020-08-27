from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

class BlogView(ListView):
    template_name = "blog.html"
    model = Blog

class BlogDetailView(DetailView):
    template_name = "blog_detail.html"
    model = Blog