# Generated by Django 4.1.1 on 2022-10-12 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugosite', '0009_alter_genre_options_remove_genre_chapter_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={},
        ),
        migrations.AddField(
            model_name='video',
            name='genres',
            field=models.ManyToManyField(blank=True, help_text='このプレイリストのジャンルを選んでください', to='ugosite.genre'),
        ),
    ]
