# Generated by Django 4.1.1 on 2023-03-25 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatment_center', '0005_alter_treatmentcity_options_alter_factor_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatmentcenter',
            name='url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
