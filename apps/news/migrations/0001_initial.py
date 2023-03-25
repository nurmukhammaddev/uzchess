# Generated by Django 4.1.7 on 2023-03-25 11:01

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='news/photos/%Y/%m/%d')),
                ('created', models.DateField(auto_now_add=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('view', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'NewArticle',
                'verbose_name_plural': 'NewArticle',
            },
        ),
        migrations.CreateModel(
            name='NewArticleView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('device_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Device ID')),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new_views', to='news.newarticle', verbose_name='News')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_views', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'New Article View',
                'verbose_name_plural': 'New Article View',
            },
        ),
    ]
