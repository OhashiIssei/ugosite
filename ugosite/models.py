from operator import contains
from django.db import models

from datetime import date
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User #Blog author or commenter

# import uuid # Required for unique comment instances

class Genre(models.Model):
    """ジャンルを表すモデル"""

    TYPE_CHOICES = [
        ('SUB', '科目'),
        ('CHA', '章'),
        ('SEC', '節'),
        ('SSE', '分節'),
        ('STU', '研究'),
        ('DEV', '発展'),
        ('SUP', '補足'),
        ('PRA', '演習'),
    ]

    name = models.CharField(
        max_length=200, 
        help_text='投稿のジャンルを入力してください'
        )
    title = models.CharField(max_length=200,null=True,blank=True,help_text='このジャンルのタイトル入力してください')
    slug =  models.SlugField(null=True,blank=True, max_length=100,  help_text='詳細ページurlに用いる文字列を入力してください')
    parent_genre = models.ForeignKey("Genre", on_delete = models.SET_NULL, null=True,blank=True,help_text='親ジャンルを指定してください')
    type = models.CharField(max_length=200, choices = TYPE_CHOICES,null=True,blank=True,help_text='このジャンルの科目してください')
    icon = models.CharField(max_length=10000,null=True,blank=True,help_text='このジャンルのアイコンSVG')

    # class Meta:
    #     ordering = ['type']

    def descendants(self):##子孫(自分も含む)
        descendants = [Genre.objects.filter(slug = self.slug)[0]]
        generation = self.children()
        genres = descendants
        while generation:
            genres = []
            for genre in generation:
                descendants += [genre]
                for child in genre.children():
                    genres += [child]
            generation = genres
        return descendants

    def videos_num(self):##(自分を含む)子孫のビデオ
        videos = []
        for genre in self.descendants():
            vs = Video.objects.filter(genres = genre)
            for v in vs:
                videos += [v]
        return len(videos)

    def problems_num(self):##(自分を含む)子孫のビデオ
        problems = []
        for genre in self.descendants():
            vs = Problem.objects.filter(genres = genre)
            for v in vs:
                problems += [v]
        return len(problems)
    
    def children(self):##子供
        return Genre.objects.filter(parent_genre = self)

    def ancestors(self):##先祖(自分含まない)
        ancestors = []
        genre = Genre.objects.filter(slug = self.slug)[0]
        # print(self.parent_genre)
        while genre.parent_genre:
            ancestors.insert(0,genre.parent_genre)
            genre = genre.parent_genre
        return ancestors

    def depth(self):
        return len(self.ancestors())
    
    def display_ancestors(self):
        ancestors = []
        for genre in self.ancestors():
            ancestors.append(genre.name)
        return ">".join(ancestors)
    
    display_ancestors.short_description = 'Ancesors'
    
    def get_absolute_url(self):
        return reverse('genre-detail', args=[self.slug])

    def __str__(self):
        return self.name

from urllib.parse import quote

class Term(models.Model):
    """用語を表すモデル"""
    name = models.CharField(max_length=200, help_text='用語名を入力してください')
    hurigana = models.CharField(max_length=200, default="ふりがな" ,help_text='ふりがなを入力してください')
    en_name = models.CharField(max_length=200, null=True, blank=True, help_text='英語名を入力してください')
    slug =  models.SlugField(null=True,blank=True, max_length=20,  help_text='詳細ページurlに用いる文字列を入力してください')
    description = models.TextField(max_length=1000, null=True, blank=True, help_text='この用語の説明を入力してください')
    genres = models.ManyToManyField(Genre, blank=True, help_text='この用語のジャンルを選んでください')
    related_terms = models.ManyToManyField("Term", blank=True, help_text='この用語に関連する用語を選んでください')

    class Meta:
        ordering = ['hurigana']

    def get_absolute_url(self):
        return reverse('term-detail', args=[self.slug])

    def videos_num(self):
        return Video.objects.filter(terms = self).count()
    
    def __str__(self):
        return self.name

class Article(models.Model):
    """記事を表すモデル"""
    # title = models.CharField(max_length=200, help_text='記事のタイトルを入力してください')
    name = models.CharField(max_length=200,null=True,blank=True,  help_text='記事のタイトルを入力してください')
    slug =  models.SlugField(max_length=20,null=True,blank=True, help_text='詳細ページurlに用いる文字列を入力してください')
    description = models.TextField(max_length=1000,blank=True, help_text='記事の説明を入力してください')
    content = models.TextField(max_length=2000,blank=True, help_text='記事の内容をHTML形式で入力してください')
    created_date = models.DateTimeField(auto_now_add=True)
    terms = models.ManyToManyField(Term, blank=True, help_text='この記事に関連する用語を選んでください')
    modules = models.ManyToManyField('Module', blank=True, help_text='この記事を含むモジュールを選んでください')
    problems = models.ManyToManyField("Problem", blank=True, help_text='この記事に含まれる問題を選んでください')

    class Meta:
        ordering = ['-created_date']


    def genres(self):#記事のジャンルは、記事が含まれるモジュールのジャンル、ということにします。ということで、記事のモジュールは必須ということです。
        genres = []
        for module in self.modules.all():
            for genre in module.genres.all():
                if genre not in genres: #同じgenreが重複しないように
                    genres += [genre]
        return genres
        # return ', '.join([genre.name for genre in self.genres.all()[:3]])

    # display_genre.short_description = 'Genre'

    def display_module(self):
        return ', '.join([module.name for module in self.modules.all()[:3]])

    display_module.short_description = 'Module'

    def ancestors(self):##先祖(自分含まない)
        article = Article.objects.get(id = self.id)
        module = article.modules.first()
        ancestors = [module]
        while module.parent_module:
            ancestors.insert(0,module.parent_module)
            module = module.parent_module
        return ancestors

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.slug)])

    def __str__(self):
        return self.name

PLAYLIST_TYPE_CHOICES = [
    ('C', '単元別'),
    ('T', 'テーマ別'),
    ('O', 'その他'),
]

class Module(models.Model):
    """モジュールを表すモデル"""
    name = models.CharField(max_length=200,null=True,blank=True,  help_text='モジュール名を入力してください')
    slug =  models.SlugField(max_length=100,null=True,blank=True, help_text='詳細ページurlに用いる文字列を入力してください')
    description = models.TextField(max_length=10000, blank=True,help_text='この用語の説明を入力してください')
    genres = models.ManyToManyField(Genre, blank=True, help_text='このモジュールのジャンルを選んでください')
    type =  models.CharField(max_length=200, choices = PLAYLIST_TYPE_CHOICES,null=True,blank=True,help_text='このモジュールの種類を選択してください')
    parent_module = models.ForeignKey("Module", on_delete = models.SET_NULL, null=True,blank=True, help_text='親モジュールを選んでください')
    # problems = models.ManyToManyField("Problem", blank=True, help_text='この記事に含まれる問題を選んでください')

    # class Meta:
    #     ordering = ['slug']

    def child_modules(self):
        return Module.objects.filter(parent_module = self)

    def child_articles(self):
        return Article.objects.filter(modules = self)

    def child_articles_num(self):
        return len(self.child_articles())

    def articles_num(self):
        num = self.child_articles_num()
        for module in self.child_modules():
            num += module.articles_num()
        return num

    def ancestors(self):##先祖(自分含まない)
        module = Module.objects.get(id = self.id)
        ancestors = []
        while module.parent_module:
            ancestors.insert(0,module.parent_module)
            module = module.parent_module
        return ancestors

    def display_genre(self):
        if self.genres.all():
            texts = []
            for genre in self.genres.all():
                texts.append(genre.display_ancestors())
            return "\n,".join(texts)

    display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        return reverse('module-detail', args=[str(self.slug)])
    
    def display_description(self):
        desc_len = 10
        if len(self.description)>desc_len:
            string=self.description[:desc_len] + '...'
        else:
            string=self.description
        return string

    def __str__(self):
        return self.name


class Problem(models.Model):
    """問題を表すモデル"""
    name = models.CharField(max_length=200, help_text='問題名を入力してください')
    slug =  models.SlugField(max_length=100, null=True,blank=True, help_text='問題ページurlに用いる文字列を入力してください')
    text = models.TextField(max_length=1000, blank=True,help_text='この問題の内容をTeX形式で入力してください')
    source = models.CharField(max_length=200, null=True,blank=True, help_text='この問題のの引用元を入力してください')
    answer = models.TextField('example_answer', max_length=10000, null=True,blank=True,help_text='この問題の解答例をTeX形式で入力してください')
    # article = models.ForeignKey(Article, on_delete = models.SET_NULL, null=True,blank=True,)
    genres = models.ManyToManyField(Genre,blank=True, help_text='ジャンルを選んでください')

    def get_admin_url(self):
        return "http://127.0.0.1:8000/admin/ugosite/problem/%s/" % self.id
    
    def get_absolute_url(self):
        return reverse('problem-detail', args=[str(self.slug)])

    def display_genre(self):
        if self.genres.all():
            texts = []
            for genre in self.genres.all():
                texts.append(genre.display_ancestors())
            return "\n,".join(texts)

    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.name

# class Source(models.Model):
#     name = models.CharField(max_length=200, help_text='引用名を入力してください')
#     slug =  models.SlugField(max_length=100, null=True,blank=True, help_text='文字列を入力してください')
#     univ = models.CharField(max_length=200,null=True,blank=True)
#     division = models.CharField(max_length=200, null=True,blank=True)
#     year = models.CharField(max_length=4, null=True,blank=True)
#     num = models.IntegerChoices(max_length=1, null=True,blank=True)
#     problem = models.ForeignKey(Problem, null=True,blank=True)
#     def __str__(self):
#         return self.univ

from django.utils import timezone
from django.contrib import admin


from django.db import models
from django_mysql.models import ListCharField

class Video(models.Model):
    """動画を表すモデル"""
    name = models.CharField(max_length=200,null=True,blank=True, help_text='問題名を入力してください')
    title = models.CharField(max_length=200, null=True,blank=True, help_text='この動画のタイトルを入力してください')
    slug = models.SlugField(max_length=100, null=True,blank=True,help_text='解説動画のYoutubeIDを入力してください')
    problems = models.ManyToManyField(Problem,blank=True, help_text='問題を指定してください')
    table = ListCharField(base_field=models.CharField(max_length=50),max_length=(50 * 20),null=True,blank=True,help_text='この動画の目次を入力してください')
    description = models.TextField(max_length=10000, null=True,blank=True, help_text='この動画の説明を入力してください')
    terms = models.ManyToManyField(Term, blank=True,help_text='この記事に関連する用語を選んでください')
    pub = models.DateTimeField(default = timezone.now)
    data = models.JSONField(null=True, help_text='このFieldはYoutubeAPIによって読み込まれます。')
    genres = models.ManyToManyField(Genre,blank=True, help_text='ジャンルを選んでください')

    # class Meta:
    #     ordering = ["pub"]

    def display_problem(self):
        if self.problems.all():
            texts = []
            for problem in self.problems.all():
                texts.append(problem.name)
            return "\n,".join(texts)

    display_problem.short_description = 'Problems'

    def display_genre(self):
        if self.genres.all():
            texts = []
            for genre in self.genres.all():
                texts.append(genre.display_ancestors())
            return "\n,".join(texts)

    display_genre.short_description = 'Genre'
            
    def get_absolute_url(self):
        return reverse('video-detail', args=[str(self.slug)])

    def __str__(self):
        return self.name

class Playlist(models.Model):
    """プレイリストを表すモデル"""
    type =  models.CharField(max_length=200, choices = PLAYLIST_TYPE_CHOICES,null=True,blank=True,help_text='このプレイリストの科目してください')
    name = models.CharField(max_length=200,null=True,blank=True,help_text='このプレイリストの名前入力してください')
    title = models.CharField(max_length=200,null=True,blank=True,help_text='このプレイリストのタイトル入力してください')
    slug = models.SlugField(max_length=100,null=True,blank=True, help_text='このプレイリストのYoutubeIDを入力してください')
    description = models.TextField(max_length=10000, null=True,help_text='このプレイリストの説明を入力してください')
    videos = models.ManyToManyField(Video,blank=True,help_text='このプレイリストが含む動画を選んでください')
    genres = models.ManyToManyField(Genre,blank=True,  help_text='このプレイリストのジャンルを選んでください')
    data = models.JSONField(null=True, help_text='このFieldはYoutubeAPIによって読み込まれます。')

    class Meta:
        ordering = ['type','title']
    
    def videos_num(self):
        return self.videos.all().count()
    
    def get_absolute_url(self):
        return reverse('playlist-detail', args=[str(self.slug)])

    def display_video(self):
        return ', '.join([video.title for video in self.videos.all()[:3]])

    display_video.short_description = 'Video'

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genres.all()[:3]])

    display_genre.short_description = 'Genre'

    def __str__(self):
        return str(self.name)

class Comment(models.Model):
    """コメントを表すモデル"""
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=1000, help_text='このコメントの内容を入力してください')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular comment')
    
    class Meta:
        ordering = ['date']

    def get_absolute_url(self):
        return reverse('comment-create', args=[str(self.id)])

    def __str__(self):
        len_title=10
        if len(self.content)>len_title:
            titlestring=self.content[:len_title] + '...'
        else:
            titlestring=self.content
        return titlestring

class Folder(models.Model):
    """フォルダを表すモデル"""
    name = models.CharField(max_length=200, null=True,blank=True, help_text='このフォルダの名前')
    path = models.CharField(max_length=200, null=True,blank=True, help_text='このフォルダのpathを入力してください')
    folders = models.ManyToManyField("Folder", blank=True, help_text='このフォルダが含まれるフォルダを指定してください')
    created_date = models.DateTimeField(default=timezone.now, blank=True, help_text='このフォルダの作成日を指定してください')
    update_date = models.DateTimeField(default=timezone.now, blank=True, help_text='このフォルダの更新日を指定してください')

    def ancestors(self):##先祖(自分含まない)
        folder =  Folder.objects.get(id = self.id)
        ancestors = []
        while folder.folders.first():
            ancestors.insert(0,folder.folders.first())
            folder = folder.folders.first()
        return ancestors
    
    def child_folders(self):
        return Folder.objects.filter(folders = self)

    def child_notes(self):
        return Note.objects.filter(folders = self)

    def child_notes_num(self):
        return len(self.child_notes())

    def notes_num(self):
        num = self.child_notes_num()
        for folder in self.child_folders():
            num += folder.notes_num()
        return num


    def get_absolute_url(self):
        return reverse('folder-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Note(models.Model):
    """ノートを表すモデル"""
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True,blank=True, help_text='このノートの名前')
    title = models.CharField(max_length=200, null=True,blank=True, help_text='このノートのタイトルを入力してください')
    path = models.CharField(max_length=200, null=True,blank=True, help_text='このノートのpathを入力してください')
    text = models.TextField(max_length=10000, blank=True,help_text='このノートの内容を入力してください')
    folders = models.ManyToManyField(Folder, blank=True, help_text='このノートのフォルダを指定してください')
    created_date = models.DateTimeField(default=timezone.now, blank=True, help_text='このノートの作成日を指定してください')
    update_date = models.DateTimeField(default=timezone.now, blank=True, help_text='このノートの更新日を指定してください')
    
    class Meta:
        ordering = ['-created_date']

    def get_absolute_url(self):
        return reverse('note-detail', args=[str(self.id)])

    def ancestors(self):##先祖(自分含まない)
        folder =  Note.objects.get(id = self.id)
        ancestors = []
        while folder.folders.first():
            ancestors.insert(0,folder.folders.first())
            folder = folder.folders.first()
        return ancestors

    def __str__(self):
        return self.title




