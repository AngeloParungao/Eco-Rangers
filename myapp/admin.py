# admin.py
from django.contrib import admin
from .models import Article, Subtopic, Activity


class ActivityInline(admin.TabularInline):  # Use TabularInline or StackedInline
    model = Activity
    extra = 1  # Number of empty activity forms shown by default


class SubtopicInline(admin.StackedInline):  # For a detailed view
    model = Subtopic
    extra = 1
    inlines = [ActivityInline]  # Nest ActivityInline inside SubtopicInline


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'content')
    list_filter = ('date',)
    inlines = [SubtopicInline]  # Add Subtopic inline editing


@admin.register(Subtopic)
class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'article')
    search_fields = ('title', 'description')
    list_filter = ('article',)
    inlines = [ActivityInline]  # Add Activity inline editing


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtopic', 'activity_type')
    search_fields = ('title', 'description')
    list_filter = ('activity_type',)
