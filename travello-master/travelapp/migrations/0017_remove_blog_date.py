# Generated by Django 3.2.10 on 2022-01-11 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0016_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='date',
        ),
    ]
