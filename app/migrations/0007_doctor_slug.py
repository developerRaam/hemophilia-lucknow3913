# Generated by Django 4.1.1 on 2023-02-23 15:11

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_historyhemophilia'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
    ]
