# Generated by Django 3.2.10 on 2022-01-11 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0015_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='pictures')),
            ],
        ),
    ]
