# Generated by Django 4.1.1 on 2023-04-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_activitypost_hindi_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='hindi_title',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Hindi Title'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=255, verbose_name='English Title'),
        ),
    ]
