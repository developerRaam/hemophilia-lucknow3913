# Generated by Django 4.1.1 on 2023-01-19 11:30

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='precosanCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Precosan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(blank=True, max_length=400, null=True)),
                ('pr_image', models.ImageField(blank=True, null=True, upload_to='precosan/')),
                ('english_description', tinymce.models.HTMLField(blank=True, null=True)),
                ('hindi_description', tinymce.models.HTMLField(blank=True, null=True)),
                ('post_by', models.CharField(default='admin', max_length=50)),
                ('views', models.IntegerField(default='0', editable=None)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.precosancategory')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(blank=True, max_length=400, null=True)),
                ('news_image', models.ImageField(blank=True, null=True, upload_to='news/')),
                ('english_description', tinymce.models.HTMLField(blank=True, null=True)),
                ('hindi_description', tinymce.models.HTMLField(blank=True, null=True)),
                ('views', models.IntegerField(default='0', editable=None)),
                ('post_by', models.CharField(default='admin', max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='news_title', unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('news_category', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.newscategory')),
            ],
        ),
    ]
