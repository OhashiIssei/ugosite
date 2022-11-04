# Generated by Django 4.1.1 on 2022-10-12 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugosite', '0006_alter_video_options_genre_parent_alter_genre_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='type',
            field=models.CharField(blank=True, choices=[('S', '科目'), ('C', '章'), ('SE', '節'), ('SS', '分節'), ('L', '補'), ('D', '発展'), ('S', '研究')], help_text='このジャンルの科目してください', max_length=200, null=True),
        ),
    ]