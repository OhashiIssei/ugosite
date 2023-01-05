# Generated by Django 4.1.1 on 2022-12-27 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0003_videoonapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoonapp',
            name='genre',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='videoonapp',
            name='point',
            field=models.TextField(default=None, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='videoonapp',
            name='problem',
            field=models.TextField(default=None, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='videoonapp',
            name='source',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='videoonapp',
            name='table',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='videoonapp',
            name='title',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
