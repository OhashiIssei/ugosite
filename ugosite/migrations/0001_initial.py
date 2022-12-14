# Generated by Django 4.1.1 on 2022-11-20 09:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='記事のタイトルを入力してください', max_length=200)),
                ('title', models.CharField(blank=True, help_text='記事のタイトルを入力してください', max_length=200)),
                ('path', models.CharField(blank=True, default='/', help_text='このカテゴリのpathを入力してください', max_length=200)),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='このカテゴリの作成日を指定してください')),
                ('update_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='このカテゴリの更新日を指定してください')),
                ('playlistId', models.SlugField(blank=True, help_text='このカテゴリのYoutubeIDを入力してください', max_length=100, null=True)),
                ('data', models.JSONField(help_text='このFieldはYoutubeAPIによって読み込まれます。', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='問題名を入力してください', max_length=200)),
                ('text', models.TextField(help_text='この問題の内容をTeX形式で入力してください', max_length=1000)),
                ('answer', models.TextField(blank=True, help_text='この問題の解答例をTeX形式で入力してください', max_length=10000, null=True, verbose_name='example_answer')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='引用名を入力してください', max_length=200)),
                ('univ', models.CharField(blank=True, max_length=200)),
                ('division', models.CharField(blank=True, max_length=200)),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TagForYoutube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='用語名を入力してください', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='用語名を入力してください', max_length=200)),
                ('hurigana', models.CharField(default='ふりがな', help_text='ふりがなを入力してください', max_length=200)),
                ('en_name', models.CharField(blank=True, help_text='英語名を入力してください', max_length=200)),
                ('description', models.TextField(blank=True, help_text='この用語の説明を入力してください', max_length=1000)),
                ('related_terms', models.ManyToManyField(help_text='この用語に関連する用語を選んでください', to='ugosite.term')),
            ],
            options={
                'ordering': ['hurigana'],
            },
        ),
        migrations.CreateModel(
            name='YoutubeChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channelId', models.CharField(help_text='チャンネルのYoutubeIDを入力してください', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='YoutubePlaylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField(help_text='このFieldはYoutubeAPIによって読み込まれます。')),
            ],
        ),
        migrations.CreateModel(
            name='YoutubePlaylistItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField(help_text='このFieldはYoutubeAPIによって読み込まれます。')),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField(help_text='このFieldはYoutubeAPIによって読み込まれます。')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('myfile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ugosite.myfile')),
                ('description', models.TextField(blank=True, help_text='記事の説明を入力してください', max_length=1000)),
                ('content', models.TextField(blank=True, help_text='記事の内容をHTML形式で入力してください', max_length=2000)),
                ('type', models.CharField(choices=[('BAS', '基本'), ('STU', '研究'), ('DEV', '発展'), ('SUP', '補足'), ('PRA', '演習'), ('TER', 'テーマ'), ('CAT', 'カテゴリ'), ('NOT', 'ノート'), ('OTH', 'その他')], default='OTH', help_text='このカテゴリの種類を選択してください', max_length=200)),
            ],
            options={
                'ordering': ['created_date'],
            },
            bases=('ugosite.myfile',),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('myfile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ugosite.myfile')),
                ('description', models.TextField(blank=True, help_text='このカテゴリの説明を入力してください', max_length=10000)),
                ('type', models.CharField(choices=[('SUB', '科目'), ('CHA', '章'), ('SEC', '節'), ('SSE', '分節'), ('TER', 'テーマ'), ('OTH', 'その他')], default='OTH', help_text='このカテゴリの種類を選択してください', max_length=200)),
                ('icon', models.CharField(blank=True, help_text='このカテゴリのアイコンSVG', max_length=10000)),
                ('parent', models.ForeignKey(help_text='この記事の親カテゴリ選んでください', null=True, on_delete=django.db.models.deletion.CASCADE, to='ugosite.category')),
            ],
            options={
                'ordering': ['created_date'],
            },
            bases=('ugosite.myfile',),
        ),
        migrations.CreateModel(
            name='DownloadedYoutubePlaylist',
            fields=[
                ('youtubeplaylist_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ugosite.youtubeplaylist')),
            ],
            bases=('ugosite.youtubeplaylist',),
        ),
        migrations.CreateModel(
            name='DownloadedYoutubePlaylistItem',
            fields=[
                ('youtubeplaylistitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ugosite.youtubeplaylistitem')),
            ],
            bases=('ugosite.youtubeplaylistitem',),
        ),
        migrations.CreateModel(
            name='DownloadedYoutubeVideo',
            fields=[
                ('youtubevideo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ugosite.youtubevideo')),
            ],
            bases=('ugosite.youtubevideo',),
        ),
        migrations.CreateModel(
            name='NewCreatedYoutubePlaylist',
            fields=[
                ('youtubeplaylist_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ugosite.youtubeplaylist')),
            ],
            bases=('ugosite.youtubeplaylist',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='この動画名前を入力してください', max_length=200)),
                ('data', models.JSONField(help_text='このFieldはYoutubeAPIによって読み込まれます。')),
                ('title', models.CharField(blank=True, help_text='この動画のタイトルを入力してください', max_length=200)),
                ('description', models.TextField(blank=True, help_text='この動画の説明を入力してください', max_length=10000)),
                ('question', models.TextField(blank=True, help_text='この動画の問題テキストを入力してください', max_length=1000)),
                ('table', django_mysql.models.ListCharField(models.CharField(max_length=50), help_text='この動画の目次を入力してください', max_length=1000, null=True, size=None)),
                ('videoId', models.CharField(blank=True, help_text='解説動画のYoutubeIDを入力してください', max_length=100)),
                ('pub', models.DateTimeField(default=django.utils.timezone.now)),
                ('problem', models.ForeignKey(help_text='問題を指定してください', on_delete=django.db.models.deletion.CASCADE, to='ugosite.problem')),
                ('related_terms', models.ManyToManyField(help_text='この記事に関連する用語を選んでください', to='ugosite.term')),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='source',
            field=models.ForeignKey(help_text='この問題のソースを選んでください', null=True, on_delete=django.db.models.deletion.CASCADE, to='ugosite.source'),
        ),
        migrations.CreateModel(
            name='Update_From_Source',
            fields=[
                ('category_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ugosite.category')),
            ],
            bases=('ugosite.category',),
        ),
        migrations.CreateModel(
            name='Update_To_Source',
            fields=[
                ('category_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ugosite.category')),
            ],
            bases=('ugosite.category',),
        ),
        migrations.CreateModel(
            name='UpdatedYoutubeVideo',
            fields=[
                ('youtubevideo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ugosite.youtubevideo')),
                ('downloadedVideo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ugosite.downloadedyoutubevideo')),
            ],
            bases=('ugosite.youtubevideo',),
        ),
        migrations.CreateModel(
            name='UpdatedYoutubePlaylist',
            fields=[
                ('youtubeplaylist_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ugosite.youtubeplaylist')),
                ('downloadedPlaylist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ugosite.downloadedyoutubeplaylist')),
            ],
            bases=('ugosite.youtubeplaylist',),
        ),
        migrations.AddField(
            model_name='problem',
            name='articles',
            field=models.ManyToManyField(help_text='この問題が含まれる記事を選んでください', to='ugosite.article'),
        ),
        migrations.AddField(
            model_name='article',
            name='parent',
            field=models.ForeignKey(help_text='この記事の親カテゴリ選んでください', on_delete=django.db.models.deletion.CASCADE, to='ugosite.category'),
        ),
    ]
