from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("articles", views.articles, name="articles"),
    path("activities", views.activities, name="activities"),
    path("multimedia", views.multimedia, name="multimedia"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact")
]
