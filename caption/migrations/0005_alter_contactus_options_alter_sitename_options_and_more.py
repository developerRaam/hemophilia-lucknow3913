# Generated by Django 4.1.1 on 2023-02-28 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caption', '0004_social_facebook_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name_plural': 'Footer Contact-us'},
        ),
        migrations.AlterModelOptions(
            name='sitename',
            options={'verbose_name_plural': 'Website Name'},
        ),
        migrations.AlterModelOptions(
            name='social',
            options={'verbose_name_plural': 'Social Media Links'},
        ),
    ]