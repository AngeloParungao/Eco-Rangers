from ast import Sub
from re import sub
from django.shortcuts import get_object_or_404, render
from .models import Article, Subtopic


# Create your views here.
def home(request):
    images = ['images/globe.png']
    videos = ['videos/galaxy.mp4']
    gifs = ['videos/elf.gif']
    return render(request, "home.html", {'images': images, 'videos': videos, 'gifs': gifs})


def articles(request):
    articles = Article.objects.all().order_by(
        '-date')  # Fetch all articles, newest first

    # Create a list of tuples with article and its related subtopics
    article_subtopics = [
        (article, Subtopic.objects.filter(article=article)) for article in articles
    ]

    return render(request, "articles.html", {
        'article_subtopics': article_subtopics
    })


def subtopic_detail(request, article_slug, subtopic_id):
    article = get_object_or_404(Article, slug=article_slug)
    subtopic = get_object_or_404(Subtopic, id=subtopic_id, article=article)
    activities = subtopic.activities.all()
    return render(request, 'subtopic_detail.html', {
        'article': article,
        'subtopic': subtopic,
        'activities': activities
    })

def activities(request):
    return render(request, "activities.html")


def multimedia(request):
    images = ['images/image.png']
    return render(request, 'multimedia.html', {'images': images})
