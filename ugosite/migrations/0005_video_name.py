# Generated by Django 4.1.1 on 2022-10-10 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugosite', '0004_alter_video_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.CharField(blank=True, help_text='問題名を入力してください', max_length=200, null=True),
        ),
    ]
