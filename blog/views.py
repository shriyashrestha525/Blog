from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post


# Create your views here.
def home(request):
    return render(request, 'blog/home.html', context={'post':Post.objects.all()})

def about(request):
    return render(request, 'blog/about.html')