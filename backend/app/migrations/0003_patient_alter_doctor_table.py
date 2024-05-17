# Generated by Django 5.0.3 on 2024-05-16 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('disease', models.CharField(max_length=200)),
                ('appointmentdate', models.DateField()),
                ('languages', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelTable(
            name='doctor',
            table='app_doctor',
        ),
    ]
