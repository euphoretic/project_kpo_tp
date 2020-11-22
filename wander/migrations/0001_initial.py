# Generated by Django 3.1.3 on 2020-11-22 11:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_address', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=50)),
                ('rating', models.FloatField(max_length=3)),
                ('description', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='wander.city')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wander.place')),
            ],
        ),
        migrations.CreateModel(
            name='PosterEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(default=django.utils.timezone.now)),
                ('date_end', models.DateField(default=None, null=True)),
                ('name', models.CharField(default='add_name_event', max_length=30)),
                ('ended', models.BooleanField(default=False)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wander.place')),
            ],
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.CharField(max_length=255)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wander.place')),
            ],
        ),
    ]
