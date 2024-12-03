from ast import Sub
from re import sub
from unicodedata import category
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
    youtube_videos = [
                        {'category':'save_nature','url':'https://www.youtube.com/embed/6jQ7y_qQYUA?si=rm5m0Cbuwe0GGiSr'},
                        {'category':'science','url':'https://www.youtube.com/embed/i_jiQzoQF5M?si=5iymQKTyYFSBArP0'}, 
                        {'category':'save_nature','url':'https://www.youtube.com/embed/belXC_IoW4o'},
                        {'category':'phenomena','url':'https://www.youtube.com/embed/S6BFw4ZURZQ?si=bxHDl6-nc1mOkYk0'},
                        {'category':'save_nature','url':'https://www.youtube.com/embed/gEk6JLJNg0U?si=UD2-AqM5nzt6DE_H'}, 
                        {'category':'nature','url':'https://www.youtube.com/embed/WmVLcj-XKnM?si=TYeKmLI6Os6F24Vl'}, 
                        {'category':'issues','url':'https://www.youtube.com/embed/JaSe85Mcwp0?si=7jwvr4c2-DYIanG3'}, 
                        {'category':'phenomena','url':'https://www.youtube.com/embed/ay416AyoqRU?si=OZ2Tr13jtgYK5zxi'},
                        {'category':'nature','url':'https://www.youtube.com/embed/pkjJsYsy5cA?si=IgQrW7dNMj6CwGFu'}, 
                        {'category':'phenomena','url':'https://www.youtube.com/embed/OCjl6tp8dnw?si=hhzxAuUE0qddsDQ1'},
                        {'category':'science','url':'https://www.youtube.com/embed/zKXMaLP_T6I?si=CQupYhPjxAxi1KxU'}, 
                        {'category':'save_nature','url':'https://www.youtube.com/embed/0Puv0Pss33M?si=hxg5IA6juRi2VPAJ'}, 
                        {'category':'issues','url':'https://www.youtube.com/embed/-01T9e6VDWU?si=DOJC8Ps56lnI6E1k'},
                        {'category':'save_nature','url':'https://www.youtube.com/embed/V0lQ3ljjl40?si=jEG_keC4TkC7cszW'}, 
                        {'category':'weather','url':'https://www.youtube.com/embed/CXKj7bm4Ops?si=agFP_t3i26cAEfKi'}, 
                        {'category':'science','url':'https://www.youtube.com/embed/Z00u4mu5Iz4?si=urZLkSjWTLkttTW4'}, 
                        {'category':'issues','url':'https://www.youtube.com/embed/M9brPifwnkQ?si=Wuwl-u6DBhpgzzMW'}, 
                        {'category':'nature','url':'https://www.youtube.com/embed/jpQnKYXr1vo?si=rxF83wiaRgwrKrkU'}, 
                        {'category':'issues','url':'https://www.youtube.com/embed/OqHp03RRTDs?si=j_pfBwoSF5JtKgy-'}, 
                        {'category':'nature','url':'https://www.youtube.com/embed/QQYgCxu988s?si=oTF1N0OZwz5xfKSM'},
                        {'category':'weather','url':'https://www.youtube.com/embed/V0v1ogEYXmo?si=6-shSe4gFiL1IAUl'}, 
                        {'category':'phenomena','url':'https://www.youtube.com/embed/q8eIwmSJP0o?si=xNSpRymH8kKUowkc'},
                        {'category':'issues','url':'https://www.youtube.com/embed/t7Q7y_xjR5E?si=7-NkSSdOU9eyKuDc'}, 
                        {'category':'issues','url':'https://www.youtube.com/embed/E5cVr3HdLa4?si=3yNfqdhu43a7CaFY'}, 
                    ]
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
    return render(request, 'multimedia.html', {'youtube_videos': youtube_videos, 'images': images, 'nature': nature, 'causes': causes, 'solutions': solutions})
