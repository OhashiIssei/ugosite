# Generated by Django 4.1.1 on 2022-12-26 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugosite', '0018_delete_youtubechannel_delete_youtubechannelsection_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoonapp',
            name='genre',
            field=models.CharField(default='他', max_length=200),
        ),
        migrations.AddField(
            model_name='videoonapp',
            name='keywords',
            field=models.ManyToManyField(to='ugosite.term'),
        ),
        migrations.AddField(
            model_name='videoonapp',
            name='point',
            field=models.TextField(default='要点なし', max_length=10000),
        ),
        migrations.AddField(
            model_name='videoonapp',
            name='problem',
            field=models.TextField(default='問題なし', max_length=10000),
        ),
        migrations.AddField(
            model_name='videoonapp',
            name='source',
            field=models.CharField(default='オリジナル', max_length=200),
        ),
        migrations.AddField(
            model_name='videoonapp',
            name='table',
            field=models.CharField(default='00:00 目次なし', max_length=1000),
        ),
        migrations.AddField(
            model_name='videoonapp',
            name='title',
            field=models.CharField(default='タイトルなし', max_length=200),
        ),
        migrations.AddField(
            model_name='videoonapp',
            name='type',
            field=models.CharField(choices=[('計算', '計算問題'), ('基本', '基本事項'), ('典型', '典型問題'), ('応用', '応用問題'), ('強化', '強化問題'), ('他', 'その他')], default='他', max_length=200),
        ),
    ]
