# Generated by Django 4.1.1 on 2022-10-16 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ugosite', '0024_article_problems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='problems',
        ),
    ]
