# Generated by Django 4.1.1 on 2023-03-07 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_delete_article_remove_precosan_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitypost',
            name='post_by',
            field=models.CharField(default='admin', editable=False, max_length=50),
        ),
    ]