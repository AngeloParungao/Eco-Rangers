from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("articles", views.articles, name="articles"),
    path('articles/<slug:article_slug>/subtopics/<int:subtopic_id>/',
         views.subtopic_detail, name='subtopic_detail'),
    path("activities", views.activities, name="activities"),
    path("multimedia", views.multimedia, name="multimedia"),
]
