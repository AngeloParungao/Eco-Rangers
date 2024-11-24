from django.contrib import admin
from .models import Article, Subtopic, Activity, ActivityContent, ActivityPDF


class ActivityContentInline(admin.TabularInline):
    model = ActivityContent
    extra = 1  # Add one empty form for content sections
    fields = ('title', 'activity_type', 'content', 'image')  # Fields to display in the inline


class ActivityPDFInline(admin.TabularInline):
    model = ActivityPDF
    extra = 1  # Add one empty form for PDF uploads
    fields = ('pdf_file', 'description')  # Display PDF file and its description


class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 1
    show_change_link = True  # Add edit links for Activity
    fields = ('title', 'subtopic')  # Display relevant fields in the inline


class SubtopicInline(admin.StackedInline):
    model = Subtopic
    extra = 1
    fields = ('title', 'article', 'description')  # Display title, article, and description


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'slug')  # Display title, date, and slug for each article
    search_fields = ('title', 'content')
    list_filter = ('date',)
    inlines = [SubtopicInline]  # Inline editing for Subtopics


@admin.register(Subtopic)
class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'article', 'description')  # Include description for clarity
    search_fields = ('title', 'description')
    list_filter = ('article',)
    inlines = [ActivityInline]  # Inline editing for Activities


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtopic', 'get_activity_types')  # Display activity type along with title and subtopic
    search_fields = ('title', 'description')
    list_filter = ('subtopic',)
    inlines = [ActivityContentInline, ActivityPDFInline]  # Inline editing for Contents and PDFs

    def get_activity_types(self, obj):
        # Collect and display all related activity types
        activity_types = ", ".join([content.get_activity_type_display() for content in obj.contents.all()])
        return activity_types if activity_types else "No activity type"
    get_activity_types.short_description = "Activity Types"  # Set a readable name for the column


@admin.register(ActivityPDF)
class ActivityPDFAdmin(admin.ModelAdmin):
    list_display = ('activity', 'pdf_file', 'description')  # Show activity and file name
    search_fields = ('pdf_file',)
    list_filter = ('activity',)
