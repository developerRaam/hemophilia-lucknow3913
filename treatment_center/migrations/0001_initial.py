# Generated by Django 4.1.1 on 2023-03-23 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factor_name', models.CharField(max_length=100)),
                ('status', models.SmallIntegerField(choices=[(1, 'Available'), (0, 'Not Available')], default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
                ('status', models.SmallIntegerField(choices=[(1, 'Available'), (0, 'Not Available')], default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Treatment City',
            },
        ),
        migrations.CreateModel(
            name='TreatmentCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50)),
                ('room_no', models.CharField(max_length=50)),
                ('doctor_photo', models.CharField(max_length=50)),
                ('hospital_name', models.CharField(max_length=255)),
                ('status', models.SmallIntegerField(choices=[(1, 'Available'), (0, 'Not Available')], default=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treatment_center.treatmentcity', verbose_name='City')),
                ('factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treatment_center.factor', verbose_name='Factor')),
            ],
            options={
                'verbose_name_plural': 'Treatment Center',
            },
        ),
    ]
