# Generated by Django 4.1.1 on 2022-10-12 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugosite', '0011_genre_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='genres',
            field=models.ManyToManyField(blank=True, help_text='ジャンルを選んでください', to='ugosite.genre'),
        ),
    ]