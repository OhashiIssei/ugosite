# Generated by Django 4.1.1 on 2022-10-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugosite', '0028_folder_path_note_name_alter_folder_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='path',
            field=models.CharField(blank=True, help_text='このノートのpathを入力してください', max_length=200, null=True),
        ),
    ]