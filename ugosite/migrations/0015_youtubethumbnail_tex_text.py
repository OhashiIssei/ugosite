# Generated by Django 4.1.1 on 2022-12-15 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugosite', '0014_rename_youtubesambnail_youtubethumbnail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubethumbnail',
            name='tex_text',
            field=models.TextField(null=True),
        ),
    ]
