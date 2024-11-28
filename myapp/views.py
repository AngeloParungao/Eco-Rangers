from ast import Sub
from re import sub
from django.shortcuts import get_object_or_404, render
from .models import Article, Subtopic


# Create your views here.
def home(request):
    nature_images = ['images/solutions/nature.png', 'images/solutions/nature2.png',
                     'images/solutions/nature3.png', 'images/solutions/nature4.png',
                     'images/solutions/nature5.png', 'images/solutions/nature6.png',
                     'images/solutions/nature7.png', 'images/solutions/nature8.png',
                     'images/solutions/nature9.png', 'images/solutions/nature10.png',
                     'images/solutions/nature11.png', 'images/solutions/nature12.png']
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
    nature = ['images/nature/image.png', 'images/nature/image2.png', 
              'images/nature/image3.png', 'images/nature/image4.png',
              'images/nature/image5.png', 'images/nature/image6.png',
              'images/nature/image7.png', 'images/nature/image8.png',
              'images/nature/image9.png', 'images/nature/image10.png',]
    causes = ['images/causes/destroyer.png', 'images/causes/destroyer2.png',
              'images/causes/destroyer3.png', 'images/causes/destroyer4.png',
              'images/causes/destroyer5.png', 'images/causes/destroyer6.png',
              'images/causes/destroyer7.png',]
    solutions = ['images/solutions/nature.png', 'images/solutions/nature2.png',
                     'images/solutions/nature3.png', 'images/solutions/nature4.png',
                     'images/solutions/nature5.png', 'images/solutions/nature6.png',
                     'images/solutions/nature7.png', 'images/solutions/nature8.png',
                     'images/solutions/nature9.png', 'images/solutions/nature10.png',
                     'images/solutions/nature11.png', 'images/solutions/nature12.png']
    images = ['images/image.png']
    return render(request, 'multimedia.html', {'images': images, 'nature': nature, 'causes': causes, 'solutions': solutions})
