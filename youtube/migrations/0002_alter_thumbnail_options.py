# Generated by Django 4.1.1 on 2022-12-26 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thumbnail',
            options={'ordering': ['id']},
        ),
    ]
