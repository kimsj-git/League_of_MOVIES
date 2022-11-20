# Generated by Django 3.2.13 on 2022-11-20 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('poster_path', models.CharField(max_length=100)),
                ('overview', models.CharField(max_length=500)),
                ('vote_average', models.FloatField(default=0)),
                ('genres', models.ManyToManyField(to='movies.Genre')),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
                ('win_movies', models.ManyToManyField(related_name='lose_movies', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_1', to='movies.movie')),
                ('movie_1_voters', models.ManyToManyField(related_name='voted_movies_1', to=settings.AUTH_USER_MODEL)),
                ('movie_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_2', to='movies.movie')),
                ('movie_2_voters', models.ManyToManyField(related_name='voted_movies_2', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movies.match')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voted_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movies.movie')),
            ],
        ),
    ]
