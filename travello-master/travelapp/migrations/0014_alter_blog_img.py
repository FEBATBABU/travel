# Generated by Django 3.2.10 on 2022-01-11 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0013_blog_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]