# Generated by Django 4.1.1 on 2022-10-12 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ugosite', '0008_alter_genre_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['parent']},
        ),
        migrations.RemoveField(
            model_name='genre',
            name='chapter',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='subject',
        ),
    ]
