# Generated by Django 4.1.1 on 2022-12-28 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0006_rename_table_videoonapp_table_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoonapp',
            name='videoId',
            field=models.SlugField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]