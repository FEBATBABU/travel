# Generated by Django 3.2 on 2021-05-15 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0007_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(),
        ),
    ]
