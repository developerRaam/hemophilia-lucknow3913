# Generated by Django 4.1.1 on 2023-01-21 10:40

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_delete_ourteam'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutHemophilia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='hemophilia/')),
                ('english', tinymce.models.HTMLField(blank=True, null=True)),
                ('hindi', tinymce.models.HTMLField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]