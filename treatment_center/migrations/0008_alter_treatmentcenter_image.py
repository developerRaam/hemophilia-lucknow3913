# Generated by Django 4.1.1 on 2023-03-30 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment_center', '0007_treatmentcity_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatmentcenter',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='treatment_center/'),
        ),
    ]