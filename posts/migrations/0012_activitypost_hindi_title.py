# Generated by Django 4.1.1 on 2023-04-18 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_alter_activitypost_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitypost',
            name='hindi_title',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Hindi Title'),
        ),
    ]