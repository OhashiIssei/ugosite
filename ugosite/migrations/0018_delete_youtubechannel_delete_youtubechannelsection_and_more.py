# Generated by Django 4.1.1 on 2022-12-16 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
        ('ugosite', '0017_remove_update_to_source_category_ptr_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='YoutubeChannel',
        ),
        migrations.DeleteModel(
            name='YoutubeChannelSection',
        ),
        migrations.DeleteModel(
            name='YoutubePlaylist',
        ),
        migrations.DeleteModel(
            name='YoutubePlaylistItem',
        ),
        migrations.RemoveField(
            model_name='youtubevideoupdateset',
            name='videos',
        ),
        migrations.AlterField(
            model_name='videoonapp',
            name='youtube_video',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='youtube.video'),
        ),
        migrations.DeleteModel(
            name='YoutubeThumbnail',
        ),
        migrations.DeleteModel(
            name='YoutubeVideo',
        ),
        migrations.DeleteModel(
            name='YoutubeVideoUpdateSet',
        ),
    ]
