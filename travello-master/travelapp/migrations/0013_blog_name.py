# Generated by Django 3.2.10 on 2022-01-11 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0012_remove_blog_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='name',
            field=models.CharField(default=int, max_length=100),
            preserve_default=False,
        ),
    ]