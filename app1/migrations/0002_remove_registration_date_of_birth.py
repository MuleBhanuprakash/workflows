# Generated by Django 3.1.5 on 2021-01-31 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='Date_of_Birth',
        ),
    ]
