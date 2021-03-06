# Generated by Django 3.1.3 on 2020-12-16 21:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wander', '0002_auto_20201130_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite_attraction', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attraction',
            name='status',
            field=models.CharField(choices=[('opened', 'Opened'), ('closed', 'Closed')], default='opened', max_length=10),
        ),
        migrations.AddField(
            model_name='posterevent',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite_poster_event', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='posterevent',
            name='status',
            field=models.CharField(choices=[('opened', 'Opened'), ('closed', 'Closed')], default='opened', max_length=10),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite_restaurant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='status',
            field=models.CharField(choices=[('opened', 'Opened'), ('closed', 'Closed')], default='opened', max_length=10),
        ),
    ]
