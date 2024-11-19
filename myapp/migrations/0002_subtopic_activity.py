# Generated by Django 5.1.3 on 2024-11-19 02:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subtopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtopics', to='myapp.article')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('activity_type', models.CharField(choices=[('game', 'Game'), ('quiz', 'Quiz'), ('discussion', 'Discussion')], max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('subtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='myapp.subtopic')),
            ],
        ),
    ]
