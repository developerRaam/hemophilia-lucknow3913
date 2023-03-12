# Generated by Django 4.1.1 on 2023-03-06 16:40

import autoslug.fields
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_news_slug_alter_precosan_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=250)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, default=None, editable=False, max_length=255, null=True, populate_from='heading', unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='titles/')),
                ('english_description', tinymce.models.HTMLField(blank=True, null=True)),
                ('hindi_description', tinymce.models.HTMLField(blank=True, null=True)),
                ('views', models.IntegerField(default='0', editable=None)),
                ('post_by', models.CharField(default='admin', max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
