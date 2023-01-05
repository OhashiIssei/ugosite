from django.db import models

# ユーティリティ
import util.normalize as normalize
import util.text_transform as text_transform

import sys

from apiclient.discovery import build

import httplib2,os

from google_auth_oauthlib.flow import InstalledAppFlow
from apiclient.discovery import build

import youtube.update as update
import youtube.download as download

# YOUTUBE_API_Key = 'AIzaSyD-ohN5V0dlXYHjP7lSrUgKcCgXDkjpR14'
YOUTUBE_API_KEY = 'AIzaSyCSZDXmnKDlNZMy8-P7EZOK44XmHWr9Y_w'


CLIENT_SECRETS_FILE = 'client_secret.json'

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account.
SCOPES = ["https://www.googleapis.com/auth/youtube"]
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

import pickle
from google.auth.transport.requests import Request

from django.db import models

def get_authenticated_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, credentials=creds)

# youtube_with_auth = get_authenticated_service()
youtube_with_key = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

import webbrowser


class Channel(models.Model):
    channelId = models.CharField(max_length=100,help_text='チャンネルのYoutubeIDを入力してください')

    def channel_sections(self):
        query_set = ChannelSection.objects.filter(data__snippet__channelId = self.channelId)
        return list(query_set)

    def download_sections(self):#,pagetoken)
        print("チャンネル「%s」のセクションをダウンロードします" % self.channelId)
        res = youtube_with_key.channelSections().list(
            channelId = self.channelId,
            part='snippet,contentDetails',
        ).execute()
        for data in res["items"]:
            if not data["snippet"]["type"] == "multipleplaylists" : continue
            new_section = ChannelSection.objects.create(data = data)
            print("ChannelSection「%s」を新たに追加しました。" % new_section)

    def download_playlists(self):#,pagetoken)
        print("チャンネル「%s」のプレイリストをダウンロードします" % self.channelId)
        pageToken = ""
        playlists = []
        while True:
            res = youtube_with_key.playlists().list(
                channelId = self.channelId,
                part='snippet',
                maxResults = 100,
                pageToken = pageToken
            ).execute() 
            playlists.extend(res["items"])
            try:
                pageToken = res["nextPageToken"]
                continue
            except:
                break
        for data in playlists:
            Playlist.objects.create(data = data)
    
    def download_uploads_playlistItems(self):
        print("Cannnel「%s」のアップロードプレイリストをダウンロードします" % self.channelId)
        res = youtube_with_key.channels().list(
            id = self.channelId,
            part="contentDetails"
        ).execute()
        channel_data = res["items"][0]
        print(channel_data)
        pageToken = ""
        playlistItems = []
        while True:
            print("チャンネル「%s」のアップロードプレイリストのページトークン「%s」をダウンロードします" % (self.channelId,pageToken))
            playlistItems_res = youtube_with_key.playlistItems().list(
                playlistId = channel_data["contentDetails"]["relatedPlaylists"]["uploads"],
                part='snippet',
                maxResults = 100,
                pageToken = pageToken
            ).execute()
            playlistItems.extend(playlistItems_res["items"])
            # if not playlistItems_res["nextPageToken"] : 
            try:
                pageToken = playlistItems_res["nextPageToken"]
                continue
            except:
                break
        
        return [PlaylistItem(data = data) for data in playlistItems]

class ChannelSection(models.Model):
    data = models.JSONField(help_text='このFieldはYoutubeAPIによって読み込まれます。')

    def title(self):
        return self.data["snippet"]["title"]

    def __str__(self):
        return self.title()

    def playlists(self):
        playlistIds = self.data["contentDetails"]["playlists"]
        playlists = []
        for playlistId in playlistIds:
            filtered_playlists = Playlist.objects.filter(data__id = playlistId)
            if len(filtered_playlists)>1:
                print("プレイリスト「%s」は複数存在します！" % filtered_playlists[0])
                sys.exit()
            if len(filtered_playlists)==0:
                print("プレイリスト「%s」は存在しません！" % playlistId)
                return []
            playlists.append(filtered_playlists[0])
        return playlists 
    
class Playlist(models.Model):
    data = models.JSONField(help_text='このFieldはYoutubeAPIによって読み込まれます。')

    def playlistId(self):
        return self.data["id"]

    def title(self):
        return self.data["snippet"]["title"]

    def description(self):
        return self.data["snippet"]["description"]
    
    def __str__(self):
        return self.title()
    
    def playlistItems(self):
        playlistId = self.playlistId()
        items = PlaylistItem.objects.filter(data__snippet__playlistId = playlistId)
        if not items:
            print("Playlist「%s」" % (self,len(items)))
            sys.exit()
        return list(items)
    
    def download_playlistItems(self):
        playlistItems = []
        pageToken = ""
        print("プレイリスト「%s」のプレイリストアイテムをダウンロード" % self)
        while True:
            res = youtube_with_key.playlistItems().list(
                playlistId = self.playlistId(),
                part='snippet',
                maxResults = 100,
                pageToken = pageToken
            ).execute()
            playlistItems.extend(res["items"])
            try:
                pageToken = res["nextPageToken"]
                continue
            except:
                break
        for data in playlistItems:
            PlaylistItem.objects.create(data = data)
    
    def update(self):
        response = youtube_with_auth.playlists().update(
            part="snippet,status",
            body=self.data
        ).execute()
        print("プレイリスト「%s」が更新されました" % response["snippet"]["title"])
        self.data = response
        self.save()

    def rewrite_title(self):
        title = self.title()
        data = self.data
        data["snippet"]["title"] = title
        self.data = data

    def type_name(self):
        s = re.findall("\s(.*?)\d",self.title())
        if not s:return "他"
        type_name = s[0]
        if not type_name in [choice[0] for choice in VIDEO_TYPE_CHOICES]:return "他"
        return type_name
    
    def genre_name(self):
        s = re.findall("(.*?)\s",self.title())
        if not s : return "他"
        return s[0]
    
class PlaylistItem(models.Model):
    data = models.JSONField(help_text='このFieldはYoutubeAPIによって読み込まれます。')

    def title(self):
        return self.data["snippet"]["title"]
    
    def videoId(self):
        return self.data["snippet"]['resourceId']["videoId"]
    
    def playlistId(self):
        return self.data["snippet"]["playlistId"]
    
    def __str__(self):
        return self.title()
    
    def download_video(self):
        print("プレイリストアイテム「%s」のビデオをダウンロード" % self)
        res = youtube_with_key.videos().list(
            id = self.videoId(),
            part='snippet',
        ).execute()
        new_data = res["items"][0]
        try:
            old_video = Video.objects.get(data__id = new_data["id"])
            old_video.data = new_data
            old_video.save()
            print("Video「%s」のデータを更新しました" % old_video)
            return old_video
        except:
            new_video = Video.objects.create(data = new_data)
            print("Video「%s」を新たに追加しました。" % new_video)
            return 
        
    def video(self):
        try:
            return Video.objects.get(data__id = self.videoId())
        except:
            videos = Video.objects.filter(data__id = self.videoId())
            if len(videos)==0:
                print("Video「%s」は存在しません！" % self)
                if input("ダウンロードしますか？y/n")=="n": return
                return self.download_video()
            if len(videos)>1:
                print("Video「%s」は複数存在します！" % self)
                if input("ダウンロードしなおしますか？y/n")=="n": return
                videos.delete()
                return self.download_video()
            
        # print("Video「%s」を取得" % videos[0])
        

class Video(models.Model):
    data = models.JSONField(help_text='このFieldはYoutubeAPIによって読み込まれます。')
    new_data = models.JSONField(null=True,blank = True,help_text='補正後のデータです。')

    class Meta:
        ordering = ['-id']

    def videoId(self):
        return self.data["id"]
    
    def title(self):
        return self.data["snippet"]["title"]
    
    def set_title(self,title:str):
        self.new_data = self.data
        self.new_data["snippet"]["title"] = title
        return self
    
    def title_in_mytex(self):
        text = text_transform.line_to_tex(self.title())
        text = text.replace("$ ","$").replace(" $","$")
        return text
    
    def description(self):
        return self.data["snippet"]["description"]
    
    def set_description(self,text):
        self.new_data = self.data
        self.new_data["snippet"]["description"] = text
        return self
    
    def set_problem(self,text):
        self.new_data = self.data
        description = self.description()
        if not "＜問題＞" in description: return self
        description = re.sub("＜問題＞\n[\s\S]*?(\n\n|$)","＜問題＞\n%s\\1" % text,description)
        description = normalize.clean_up_lines(description)
        self.new_data["snippet"]["description"] = description
        return self
    
    def __str__(self):
        return self.title()
    
    def description(self):
        return self.data["snippet"]["description"]
    
    def extract_item(self,item_name:str):
        items = re.findall("＜%s＞\n([\s\S]*?)(?:\n\n|$)" % item_name,self.description())
        if len(items)==0:
            # print("%sは＜%s＞を含みません！" % (self,item_name))
            return None
        if len(items)>1:
            print("%sは複数の＜%s＞が記述されています！" % (self,item_name))
            return "\n\n".join(items)
            # sys.exit()
        return  items[0]
    
    def extract_item_in_jax(self,item_name:str):
        item = self.extract_item(item_name)
        if not item: return ""
        item = text_transform.text_to_tex(item)
        item = text_transform.transform_to_html_list(item)
        return item 
    
    def rewrite_title(self):
        title = self.title()
        old_title = title
        title = re.sub("\s?〜初級〜"," Lv.1",title)
        title = re.sub("\s?〜中級〜"," Lv.2",title)
        title = re.sub("\s?〜上級〜"," Lv.3",title)
        new_title =  title
        if old_title == new_title : return self
        self.set_title(title)
        print(title)
        return self
    
    def rewrite_problem(self):
        if not self.extract_item("問題"):return self
        old_text = self.extract_item("問題")
        text = old_text
        a = re.search("\\\\vec\{[a-z]\}",text)
        if not a: return self
        text = re.sub("\\\\vec\{([a-z])\}","ベクトル\\1",text)
        new_text = text
        if new_text == old_text: return self
        self.set_problem(text)
        print("\n「%s」の問題文を変更しました:\n%s\n" % (self,self.description()))
        return self
    
    def youtube_studio_url(self):
        return "https://studio.youtube.com/video/%s/edit" % self.videoId()
    
    def update(self):
        response = youtube_with_auth.videos().update(
            part="snippet,status",
            body=self.new_data
        ).execute()
        print("ビデオ「%s」が更新されました" % response["snippet"]["title"])
        self.data = response
        self.new_data  = None
        self.save()
        return self
    
    def playlists(self):
        id = self.videoId()
        return [
            Playlist.objects.get(data__id = item.playlistId())
            for item in PlaylistItem.objects.all()
            if item.videoId() == id
        ]
    
    def main_playlist(self):
        playlists = self.playlists()
        if len(playlists)==1:
            return playlists[0]
        if len(playlists)>1:
            # playlist_list = ["%s:%s" % (i,playlist.title()) for i,playlist in enumerate(playlists)]
            # select_num = int(input("Please select num playlist:%s" % ",".join(playlist_list)))
            select_num = 0
            return playlists[select_num]
        
    def redownload(self):
        print("プレイリストアイテム「%s」のビデオをダウンロード" % self)
        res = youtube_with_key.videos().list(
            id = self.videoId(),
            part='snippet',
        ).execute()
        new_data = res["items"][0]
        self = Video.objects.get(data__id = new_data["id"])
        self.data = new_data
        self.save()
        print("Video「%s」のデータを更新しました" % self)

    def extract_genre_from_playlist(self):
        playlist = self.main_playlist()
        if not playlist:return "他"
        return playlist.genre_name()

    def extract_type_from_playlist(self):
        playlist = self.main_playlist()
        if not playlist:return "他"
        return playlist.type_name()
    
    def thumbnail_url(self):
        return self.data["snippet"]["thumbnails"]["high"]["url"]

import os,re
import imagesize

import util.file_transform as file_transform

TEMPLATE_PATH = './youtube/thumbnails/templates/texs/thumbnail_template.tex'
BACKGROUND_IMAGE_DIR = "./youtube/thumbnails/templates/smart_background"

class Thumbnail(models.Model):
    youtube_video = models.ForeignKey(Video,on_delete = models.CASCADE)
    tex_text = models.TextField(null = True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return "「%s」のサムネイル" % self.youtube_video.title()

    def videoId(self):
        return self.youtube_video.videoId()

    def make_raw_text(self):
        video = self.youtube_video
        point_text = video.extract_item("要点")
        if point_text :
            return point_text
        problem_text = video.extract_item("問題")
        if problem_text:
            return problem_text
        return video.title()
    
    def title_in_mytex(self):
        video = self.youtube_video
        return video.title_in_mytex()
        
    def make_tex_page_from_description(self):
        genre_mark = self.genre_mark()
        background_image = self.background_image()
        text = self.make_tex_text_from_description()
        return background_image+genre_mark+text
    
    def background_image(self):
        image_path = self.background_image_path()
        width, height = imagesize.get(image_path)
        return "\n\n\\at(0cm,0cm){\\includegraphics[width=8cm,bb=0 0 %s %s]{%s}}\n" % (width, height,image_path)
    
    def genre_mark(self):
        video = self.youtube_video
        genre = video.extract_genre_from_playlist()
        type = video.extract_type_from_playlist()
        genre_name = genre.replace("数III","数Ⅲ").replace("数II","数Ⅱ").replace("数I","数Ｉ").replace("数A","数Ａ").replace("数B","数Ｂ")
        xpos_list = [7.2,7.2,7.2,7.2,7.0,6.8,6.6,6.4,6.2,6.0]
        xpos = xpos_list[len(genre_name)]
        return "\\at(%scm,0.2cm){\\small\\color{%s}$\\overset{\\text{%s}}{\\text{%s}}$}\n" % (xpos,"bradorange",genre_name,type)
    
    def make_tex_text_from_description(self):
        text = self.make_raw_text()
        text = text_transform.text_to_tex(text)
        text = text_transform.take_linebraek_if_list(text)
        text = text_transform.make_math_line(text)
        text = text_transform.make_array(text)
        text = text_transform.tex_to_mytex(text)
        video_title = self.title_in_mytex()
        title_size = self.calc_title_size_name()
        text_size = self.calc_text_size_name()
        return "{\\color{orange}%s\\underline{%s}}\\vspace{0.3zw}\n\n%s \n問．%s\n" % (title_size,video_title,text_size,text)
    
    def background_image_path(self):
        video_genre = self.youtube_video.extract_genre_from_playlist()
        if not video_genre:
            return ""
        image_path = "%s/%s.jpeg" % (BACKGROUND_IMAGE_DIR,video_genre)
        if os.path.isfile(image_path):
            return image_path
        return "%s/黒板風.jpeg" % BACKGROUND_IMAGE_DIR
    
    def calc_evaluation(self,text:str):
        if not text: return 0
        zenkaku_num = len(re.findall("[ぁ-んァ-ヶ一-龠々ー〜．，\+「 」αβγ]",text))
        hankaku_num = len(re.findall("[a-zA-Z\.\s\-\(\)\=\,0-9\|\<\>]",text))
        linesep_num = len(re.findall("\n",text))
        frac_num = len(re.findall("/",text))
        evaluation = zenkaku_num + hankaku_num*2/3 + linesep_num*8 +  frac_num*5
        return evaluation
    
    def calc_text_size_name(self):
        raw_text = self.make_raw_text()
        evaluation = self.calc_evaluation(raw_text)
        # print(evaluation)
        if evaluation>=200: return "\\scriptsize"
        if evaluation>=150: return "\\small"
        if evaluation>=100: return "\\normalsize"
        if evaluation>=80:  return "\\large"
        if evaluation>=50:  return "\\Large"
        if evaluation>=30:  return "\\LARGE"
        if evaluation>=15:  return "\\huge"
        return "\\HUGE"
        
    def calc_title_size_name(self):
        video = self.youtube_video
        title = video.title()
        evaluation = self.calc_evaluation(title)
        # print(evaluation)
        if evaluation>=18:  return "\\normalsize"
        if evaluation>=15:  return "\\large"
        if evaluation>=12:  return "\\Large"
        if evaluation>=9:   return "\\LARGE"
        return "\\huge"
    
import codecs,shutil,subprocess

from django.utils import timezone
from django.urls import reverse

import  util.list_edit as list_edit

class VideoUpdateSet(models.Model):
    name = models.CharField(max_length=50)
    videos = models.ManyToManyField(Video)

    def __str__(self):
        return self.name
    
    def main_dir(self):
        return "./youtube/thumbnails/%s" % self
    
    def texs_dir(self):
        return "%s/texs" % self.main_dir()
    
    def jpegs_dir(self):
        return "%s/jpegs" % self.main_dir()

    def texfile_path(self):
        return "%s/thumbnails.tex" % self.texs_dir()
    
    def old_texfile_path(self):
        return "./youtube/thumbnails/old_texs/thumbnail_%s.tex" % self
    
    def pdf_path(self):
        return "%s/thumbnails.pdf" % self.texs_dir()
    
    def jpeg_path(self):
        return "%s/thumbnails.jpeg" % self.jpegs_dir()
    
    def jpeg_with_num_path(self,i):
        return "%s/thumbnails-%s.jpeg" % (self.jpegs_dir(),i)
    
    def jpeg_with_videoId(self,video:Video):
        return "%s/%s.jpeg" % (self.jpegs_dir(),video.videoId())

    def make_from_playlist(self,playlist:Playlist):
        items = playlist.playlistItems()
        video_set = VideoUpdateSet.objects.create(name = playlist.title().replace(" ","_"))
        for item in items:
            video_set.videos.add(item.video())
        return video_set
    
    def join(self,video_sets,set_name:str):
        new_video_set = VideoUpdateSet.objects.create(name = set_name)
        for video_set in video_sets:
            new_video_set.videos.add(*video_set.videos.all())
        return new_video_set
    
    def make_dirs(self):
        main_dir_path = self.main_dir()
        texs_path = self.texs_dir()
        jpegs_path = self.jpegs_dir()
        if not os.path.isdir(main_dir_path):
            os.mkdir(main_dir_path)
            print("新たにディレクトリを作成しました:\n %s" % main_dir_path)
        if not os.path.isdir(texs_path):
            os.mkdir(texs_path)
            print("新たにディレクトリを作成しました:\n %s" % texs_path)
        if not os.path.isdir(jpegs_path):
            os.mkdir(jpegs_path)
            print("新たにディレクトリを作成しました:\n %s" % jpegs_path)
    
    def make_texfile(self):
        videos = self.videos.all()
        content_texts = []
        for video in videos:
            try:
                thumbnail = Thumbnail.objects.filter(youtube_video=video).last()
                text = thumbnail.tex_text.replace("./thumbnails","./youtube/thumbnails")
                content_texts.append(text)
                print("「%s」は保存されたデータを使用します" % video)
            except:
                thumbnail = Thumbnail(youtube_video=video)
                content_texts.append(thumbnail.make_tex_page_from_description())
                print("「%s」はdescriptionから抽出します" % video)
        content_path = self.texfile_path()
        t = codecs.open(TEMPLATE_PATH, 'r','utf-8')
        template_text = t.read()
        f = codecs.open(content_path, 'w', 'utf-8')#  % timezone.now()
        file_text = template_text.replace("{{template}}","\n\n\\newpage\n\n".join(content_texts))
        f.write(file_text)
        f.close()

    def save_each_data_form_texfile(self):
        content_path = self.texfile_path()
        f = codecs.open(content_path, 'r','utf-8')#  % timezone.now()
        all_text = f.read()
        t = re.findall("\\\\begin\{document\}([\S\s]*?)\\\\end\{document\}",all_text)
        document_text = t[0]
        document_text = normalize.clean_up_lines(document_text)
        texts = re.split("\n*\\\\newpage\n*",document_text)
        videos = self.videos.all()
        if not len(texts)==len(videos):
            input("「%s」はold_tex(%s)とplaylist(%s)の問題数が一致しません．" % (self,len(texts),len(videos)))
            sys.exit()
        for i,video in enumerate(videos):
            old_thumbnails = Thumbnail.objects.filter(youtube_video=video)
            if old_thumbnails:
                old_thumbnails.delete()
                print("サムネイルデータを上書きしました")
                continue
            thumbnail = Thumbnail.objects.create(youtube_video=video, tex_text=texts[i])
            print("%sを再利用可能データとして新規登録しました" % thumbnail)

    def back_up(self):
        print("VideoSet「%s」のバックアップファイルを作成しました" % self)
        shutil.copytree(self.main_dir(), './youtube/thumbnails/saved_sets/%s_%s' % (self,timezone.now()))

    def save_each_data_form_old_texfile(self):
        content_path = self.old_texfile_path()
        f = codecs.open(content_path, 'r','utf-8')#  % timezone.now()
        all_text = f.read()
        t = re.findall("\\\\begin\{document\}([\S\s]*?)\\\\end\{document\}",all_text)
        document_text = t[0]
        document_text = normalize.clean_up_lines(document_text)
        texts = re.split("\n*\\\\newpage\n*",document_text)
        videos = self.videos.all()
        if not len(texts)==len(videos):
            input("「%s」はold_tex(%s)とplaylist(%s)の問題数が一致しません．" % (self,len(texts),len(videos)))
        for i,video in enumerate(videos):
            text =texts[i].replace("./media_local","./youtube/thumbnails/templates")
            # if input("%s\n 上記を「%s」ののサムネイルTeXとして、保存していいですか？y/n\n:" % (text,video))=="n":return
            thumbnail = Thumbnail.objects.create(youtube_video=video,tex_text =  text)
            print("%sを個別データとして保存しました" % thumbnail)

    def ptex2pdf(self):
        dir = "./youtube/thumbnails/%s/texs" % self
        tex_path = self.texfile_path()
        file_transform.ptex2pdf(tex_path,dir)

    def open_pdf(self):
        subprocess.Popen(["open", "-a", "Preview.app",  self.pdf_path()])

    def pdf2jpeg(self):
        file_transform.pdf2jpeg(self.pdf_path(),self.jpeg_path())
        for i,video in enumerate(self.videos.all()):
            old_file_path = self.jpeg_with_num_path(i)
            new_file_path = self.jpeg_with_videoId(video)
            os.rename(old_file_path,new_file_path)

    def set_on_youtube(self):
        for video in self.videos.all():
            path = self.jpeg_with_videoId(video)
            if not os.path.isfile(path):
                input("次のファイルが見つかりません:%s" % path)
            response = youtube_with_auth.thumbnails().set(
                videoId=video.videoId(),
                media_body=path
            ).execute()
            print("ビデオ「%s」が更新されました：\n%s" % (video,response))

    def redownload(self):
        for video in self.videos.all():
            video.redownload()
        

    def create_all_video_set_list(self,max_num):
        video_list = [thumbnail.youtube_video for thumbnail in Thumbnail.objects.all()]
        video_set_list = []
        for video_list in list_edit.split_with_max_number(video_list,10):
            video_set = VideoUpdateSet.objects.create(name = "all_thumbnail")
            video_set.videos.add(*video_list)
            video_set_list.append(video_set)
        return video_set_list
    
    def create_from_keyword(self,keyword:str):
        playlists = Playlist.objects.filter(data__snippet__title__icontains = keyword)
        if not playlists:
            sys.exit()
        video_sets = [VideoUpdateSet().make_from_playlist(playlist) for playlist in playlists]
        file_name = keyword.replace(" ","_")
        return VideoUpdateSet().join(video_sets,file_name)


VIDEO_TYPE_CHOICES = [
    ('計算', '計算問題'), 
    ('基本', '基本事項'), 
    ('典型', '典型問題'), 
    ('応用', '応用問題'), 
    ('強化', '強化問題'),
    ('他', 'その他')
]
from django_mysql.models import ListCharField


ALL_THUMNAIL_DIR =  "./youtube/thumbnails/all_thumbnail/jpegs"

class VideoOnApp(models.Model): #検索と表示機能を持ったビデオ
    youtube_video = models.OneToOneField(Video,on_delete = models.CASCADE)
    videoId = models.SlugField(max_length=20)
    title = models.CharField(default = None,max_length=200)
    source = models.CharField(default = None,null=True, max_length=200)
    video_type = models.ForeignKey("VideoType",default = None,null=True,on_delete=models.SET_NULL)
    video_genre = models.ForeignKey("VideoGenre",default = None,null=True,on_delete=models.SET_NULL)
    table_list = ListCharField(
        null = True,
        base_field = models.CharField(max_length = 100),
        size = 20,
        max_length = (100 * 21)
    )
    problem = models.TextField(default = None, null=True, max_length = 10000)
    point = models.TextField(default = None ,null=True, max_length = 10000)

    class Meta:
        ordering = ['id']

    def create_from(self,video:Video):
        self.youtube_video = video
        self.videoId = video.videoId()
        self.title = video.title()
        self.source = video.extract_item("ソース")
        table_text = video.extract_item("目次")
        if table_text:
            self.table_list =table_text.replace("\n",",")
        self.problem = video.extract_item_in_jax("問題")
        self.point =video.extract_item("要点")

        self.video_type = VideoType.objects.get(name = video.extract_type_from_playlist())
        self.video_genre = VideoGenre.objects.get(name = video.extract_genre_from_playlist())

        self.save()
        return self
    
    def get_absolute_url(self):
        return reverse('video-detail', args=[str(self.id)])
    
    def description(self):
        return self.youtube_video.description()
    
    def playlists(self):
        return self.youtube_video.playlists()
    
    def __str__(self):
        return self.title
    
    def youtube_url(self):
        return "https://youtu.be/%s" % self.videoId
    
    def youtube_studio_url(self):
        return "https://studio.youtube.com/video/%s/edit" % self.videoId
    
    def thumbnail_url(self):
        local_thumnail_path = "%s/%s.jpeg" % (ALL_THUMNAIL_DIR,self.videoId)
        if os.path.isfile(local_thumnail_path):
            return "/media/all_thumbnail/jpegs/%s.jpeg" % self.videoId
        return self.youtube_video.thumbnail_url()
    
    def initialize(self):
        VideoOnApp.objects.all().delete()
        for video in Video.objects.all():
            video_on_app = VideoOnApp().create_from(video)
            print(video_on_app)

    
MY_CHANNEL_ID = "UCtEVdDYltR4eWf-QXvjmCJQ"

class VideoType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def initialize(self):
        VideoType.objects.all().delete()
        for type in VIDEO_TYPE_CHOICES:
            VideoType.objects.create(name = type[0])

class VideoGenre(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def initialize(self):
        VideoGenre.objects.all().delete()
        genre_name_list = [playlist.genre_name() for playlist in Playlist.objects.all()]
        genre_name_list = list(set(genre_name_list))
        for name in genre_name_list:
            VideoGenre.objects.create(name = name)
            


class VideoSearch(models.Model):
    keyword = models.CharField(max_length=100)
    video_types = models.ManyToManyField(VideoType)
    video_genres = models.ManyToManyField(VideoGenre)

    def __str__(self):
        return self.keyword
    
    def display_video_types(self):
        return ",".join([video_type.name for video_type in self.video_types.all()])
    
    def download_videoId_list(self):
        search_response = youtube_with_key.search().list(
            channelId = MY_CHANNEL_ID,
            type = "video",
            q = self.keyword,
            part = "id",
            maxResults = 50 ##1〜50を指定する。
        ).execute()
        return [item["id"]["videoId"] for item in search_response["items"]]

    def result_video_list(self):
        set = SearchedVideoSet.objects.create(search = self)
        # set.search_youtube()
        set.add_all_videos()
        set.filter_by_types()
        set.filter_by_genres()
        return set.video_on_app_list()
    
    def initialize(self):
        VideoSearch.objects.all().delete()
        VideoSearch.objects.create(keyword = "はやくち解説")


class SearchedVideo(models.Model):
    video = models.ForeignKey(VideoOnApp,on_delete=models.CASCADE)
    num = models.PositiveSmallIntegerField(blank=True)

    def __str__(self):
        return f'{self.num}:{self.video}'

    class Meta:
        ordering = ['num']

class SearchedVideoSet(models.Model):
    search = models.ForeignKey(VideoSearch,on_delete=models.CASCADE)
    searched_videos = models.ManyToManyField(SearchedVideo)

    def search_youtube(self):
        videoId_list = self.search.download_videoId_list()
        self.add_by_videoId_list(videoId_list)

    def add_all_videos(self):
        for num,video in enumerate(VideoOnApp.objects.all()):
            searched_video = SearchedVideo.objects.create(
                num = num,
                video = video
            )
            self.searched_videos.add(searched_video)

    def add_by_videoId_list(self,videoId_list:list):
        for num,videoId in enumerate(videoId_list):
            searched_video = SearchedVideo.objects.create(
                num = num,
                video = VideoOnApp.objects.get(videoId = videoId)
            )
            self.searched_videos.add(searched_video)

    def filter_by_videos_on_app(self,videos_list:list):
        remove_videos = self.searched_videos.exclude(video__in = videos_list)
        self.searched_videos.remove(*remove_videos.all())
    
    def filter_by_types(self):
        video_types = self.search.video_types
        self.filter_by_videos_on_app(VideoOnApp.objects.filter(video_type__in = video_types.all()))

    def filter_by_genres(self):
        video_genres = self.search.video_genres
        self.filter_by_videos_on_app(VideoOnApp.objects.filter(video_genre__in = video_genres.all()))

    def video_on_app_list(self):
        return [searched_video.video for searched_video in self.searched_videos.all()]