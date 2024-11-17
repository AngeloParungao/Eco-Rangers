from django.shortcuts import render, HttpResponse
from .models import Article


# Create your views here.
def home(request):
    return render(request, "home.html")

def articles(request):
    articles = Article.objects.all().order_by('-date')  # Fetch all articles, newest first
    return render(request, "articles.html" , {'articles': articles})

def activities(request):
    return render(request, "activities.html")

def multimedia(request):
    images = ['images/image.png']
    return render(request, 'multimedia.html', {'images': images})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")