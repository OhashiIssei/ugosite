# Generated by Django 4.1.1 on 2022-10-24 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugosite', '0038_module_parent_module_alter_module_genres_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='headline',
            field=models.CharField(help_text='記事のタイトルを入力してください', max_length=200),
        ),
    ]