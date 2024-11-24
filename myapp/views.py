from ast import Sub
from re import sub
from django.shortcuts import get_object_or_404, render
from .models import Article, Subtopic


# Create your views here.
def home(request):
    nature_images = ['images/nature/nature.png', 'images/nature/nature2.png',
                     'images/nature/nature3.png', 'images/nature/nature4.png',
                     'images/nature/nature5.png', 'images/nature/nature6.png',
                     'images/nature/nature7.png', 'images/nature/nature8.png',
                     'images/nature/nature9.png', 'images/nature/nature10.png',
                     'images/nature/nature11.png', 'images/nature/nature12.png']
    images = ['images/globe.png']
    videos = ['videos/galaxy.mp4']
    gifs = ['videos/elf.gif']
    return render(request, "home.html", {'images': images, 'videos': videos, 'gifs': gifs, 'nature_images': nature_images})


def articles(request):
    articles = Article.objects.all().order_by(
        'date')  # Fetch all articles, oldest first

    # Create a list of tuples with article and its related subtopics
    article_subtopics = [
        (article, Subtopic.objects.filter(article=article)) for article in articles
    ]

    return render(request, "articles.html", {
        'article_subtopics': article_subtopics
    })


def subtopic_detail(request, article_slug, subtopic_id):
    # Fetch the article using the slug
    article = get_object_or_404(Article, slug=article_slug)

    # Fetch the subtopic for the specific article using both subtopic_id and article
    subtopic = get_object_or_404(Subtopic, id=subtopic_id, article=article)

    # Get all activities related to the subtopic
    activities = subtopic.activities.all()

    # Return the rendered response with relevant context
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
