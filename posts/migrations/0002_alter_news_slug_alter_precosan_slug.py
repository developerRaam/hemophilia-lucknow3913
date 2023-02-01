# Generated by Django 4.1.1 on 2023-01-19 12:00

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, default=None, editable=False, null=True, populate_from='news_title', unique=True),
        ),
        migrations.AlterField(
            model_name='precosan',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]