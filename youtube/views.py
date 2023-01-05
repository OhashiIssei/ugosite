from django.shortcuts import render

import codecs

from .models import Video,Playlist,PlaylistItem,ChannelSection,Channel,Thumbnail,VideoUpdateSet,MY_CHANNEL_ID



class ThumbnailGenerator:
    def generate(self,video_set:VideoUpdateSet):
        video_set.make_dirs() # 初めてセットを作った時だけ必要
        # video_set.redownload() # Youtubeにある最新の状態を反映したいときだけONに
        video_set.make_texfile() # すでに保存されているThumbnailモデルがなければ、Video.dataから生成する。texfileを手動で編集するときはOFFにする。
        video_set.ptex2pdf() 
        video_set.open_pdf() # ビューワーで見たい時だけONにするとスムーズ。

        video_set.pdf2jpeg() # 少し時間がかかります。
        # video_set.set_on_youtube() # youtube_with_auth が必要
        # video_set.save_each_data_form_texfile() # Thumbnailモデルとして保存する。
        # video_set.back_up() # saved_setsディレクトリに保存。復元するメソッドはまだない。

    def all_video(self):
        for video_set in  VideoUpdateSet().create_all_video_set_list(10):
            self.generate(video_set)

    def by_keyword(self,keyword:str):
        self.generate(VideoUpdateSet().create_from_keyword(keyword))

# ThumbnailGenerator().by_keyword("典型")
# ThumbnailGenerator().all_video()


import os

from youtube.models import VideoOnApp

import random

class RandomPresentationSystem:
    def select(self,videos):
        random_num = random.randrange(len(videos))
        selected_video = videos[random_num]
        return selected_video

    def test():
        videos = VideoOnApp.objects.filter(data__snippet__title__icontains = "2次関数")
        video_list_for_test = list(videos)
        for i in range(10):
            test_selected_video = RandomPresentationSystem().select(video_list_for_test)
            print("test_selected: %s" % test_selected_video)
            video_list_for_test.remove(test_selected_video)
            if video_list_for_test:continue
            break
        selected_video = RandomPresentationSystem().select(videos)
        print("✨selected: %s" % selected_video)
        return selected_video
    
import django.views.generic as generic

import util.text_transform as text_transform

from youtube.models import VideoSearch


import datetime


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

import urllib.parse as parse

class VideoOnAppListView(generic.ListView):
    model = VideoOnApp
    
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import VideoSearchForm

from .models import VideoSearch,VideoType,VideoGenre

class VideoSearchView(View):
    form_class = VideoSearchForm
    initial = {'keyword': 'はやくち解説'}
    template_name = 'youtube/video_saerch.html'

    def get(self, request, *args, **kwargs):
        searchs = VideoSearch.objects.filter(id = self.kwargs["pk"])
        if not searchs:
            return render(request, self.template_name, context={'form': self.form_class()})
        search = searchs[0]
        video_list = search.result_video_list()
        context = {
            'keyword': search.keyword,
            'channel': Channel(channelId=MY_CHANNEL_ID),
            "videos_list" : video_list,
            "videos_num" : len(video_list),
            'form': self.form_class(
                initial={
                    'keyword': search.keyword, 
                    'video_types': search.video_types.all(),
                    'video_genres': search.video_genres.all()
                    }
                )
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})
        
        keyword = str(form.cleaned_data['keyword'])
        video_type_list = list(form.cleaned_data['video_types'])
        video_genre_list = list(form.cleaned_data['video_genres'])
        
        search = VideoSearch.objects.create(keyword= keyword)
        search.video_types.add(*video_type_list)
        search.video_genres.add(*video_genre_list)

        return HttpResponseRedirect(reverse('video_search', args=[search.id]))
 
class VideoOnAppDetailView(generic.DetailView):
    model = VideoOnApp
    def get_context_data(self, **kwargs):
        context = super(VideoOnAppDetailView,self).get_context_data(**kwargs)
        context["video"] = context["videoonapp"]
        return context
        

def display_status():
    print("ChannelSectionの個数: %s" % len(ChannelSection.objects.all()))
    print("Playlistの個数: %s" % len(Playlist.objects.all()))
    print("PlaylistItemの個数: %s" % len(PlaylistItem.objects.all()))
    print("Videoの個数: %s" % len(Video.objects.all()))
    print("VideoOnAppの個数: %s" % len(VideoOnApp.objects.all()))
    print("Thumbnailの個数: %s" % len(Thumbnail.objects.all()))

display_status()


# データの更新など

import youtube.download as download

# download.videos()
# download.playlists()
# download.playlistItems()
# download.sections()

# VideoType().initialize()
# VideoGenre().initialize()
# VideoOnApp().initialize()