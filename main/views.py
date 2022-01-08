from django.shortcuts import redirect, render
from .models import *

def Home(request):
    posts = Posts.objects.all()
    latest_posts = posts[::-1][:4]
    context = {'posts':posts, 'latest':latest_posts}
    return render(request, 'main/index.html', context)

def covid(request):
    posts = Posts.objects.all().filter(cat='کرونا')
    context = {'posts':posts}
    return render(request, 'main/covid.html', context)

def shohada(request):
    posts = Posts.objects.all().filter(cat='شهدا')
    context = {'posts':posts}
    return render(request, 'main/shoh.html', context)

def shahr(request):
    posts = Posts.objects.all().filter(cat='شهر')
    context = {'posts': posts}
    return render(request, 'main/shah.html', context)

def Es(request):
    return render(request, 'main/es.html')

def Detail(request, id):
    post = Posts.objects.get(id=id)
    context = {'post':post}
    return render(request, 'main/det.html', context)
