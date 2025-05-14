from django.shortcuts import render #Esta línea ya estaba así cuando la abrí (página 100)

from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = "home.html"

# Create your views here.
