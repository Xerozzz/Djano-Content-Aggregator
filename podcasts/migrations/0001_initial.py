# Generated by Django 3.2.6 on 2023-05-28 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('image', models.URLField()),
                ('link', models.URLField()),
                ('podcast_name', models.CharField(max_length=200)),
                ('guid', models.CharField(max_length=50)),
            ],
        ),
    ]
