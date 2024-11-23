# models.py
from django.db import models
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/images/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)  # Add slug field

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Auto-generate slug from the title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Subtopic(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='subtopics')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='subtopics/images/', blank=True, null=True)  # Add image field

    def __str__(self):
        return self.title


class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('game', 'Game'),
        ('quiz', 'Quiz'),
        ('discussion', 'Discussion'),
    ]

    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE, related_name='activities')
    title = models.CharField(max_length=255)
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPES)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    pdf_file = models.FileField(upload_to='activities/pdf/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.get_activity_type_display()})"
