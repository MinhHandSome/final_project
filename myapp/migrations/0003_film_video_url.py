# Generated by Django 3.2.4 on 2021-08-12 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_film_actor'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='video_url',
            field=models.CharField(default='', max_length=250),
        ),
    ]
