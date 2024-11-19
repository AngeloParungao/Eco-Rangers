from ast import Sub
from re import sub
from django.shortcuts import render, HttpResponse
from .models import Article, Subtopic


# Create your views here.
def home(request):
    images = ['images/globe.png']
    videos = ['videos/galaxy.mp4']
    gifs = ['videos/elf.gif']
    return render(request, "home.html" , {'images': images , 'videos': videos , 'gifs': gifs})

def articles(request):
    articles = Article.objects.all().order_by('-date')  # Fetch all articles, newest first
    
    # Create a list of tuples with article and its related subtopics
    article_subtopics = [
        (article, Subtopic.objects.filter(article=article)) for article in articles
    ]
    
    return render(request, "articles.html", {
        'article_subtopics': article_subtopics
    })

def activities(request):
    return render(request, "activities.html")

def multimedia(request):
    images = ['images/image.png']
    return render(request, 'multimedia.html', {'images': images})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")