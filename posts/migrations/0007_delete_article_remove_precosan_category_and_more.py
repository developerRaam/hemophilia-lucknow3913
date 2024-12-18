# Generated by Django 4.1.1 on 2023-03-07 18:22

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_rename_pr_image_posts_image_alter_posts_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.RemoveField(
            model_name='precosan',
            name='category',
        ),
        migrations.AlterModelOptions(
            name='activitypost',
            options={'verbose_name_plural': 'Activity Post'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name_plural': 'Post'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, blank=True, default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='NewsCategory',
        ),
        migrations.DeleteModel(
            name='Precosan',
        ),
        migrations.DeleteModel(
            name='precosanCategory',
        ),
    ]
