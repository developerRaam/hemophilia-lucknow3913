# Generated by Django 4.1.1 on 2023-04-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment_center', '0008_alter_treatmentcenter_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='hemophilia/')),
            ],
        ),
    ]
