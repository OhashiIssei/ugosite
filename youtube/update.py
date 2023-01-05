
MY_CHANNEL_ID = "UCtEVdDYltR4eWf-QXvjmCJQ"

def make_new_datas():
    from .models import Video
    videos = Video.objects.all()
    for i,video in enumerate(videos):
        print("\n\n%s:%s" % (i,video))
        video.rewrite_title()
        video.save()
    updated_videos = Video.objects.filter(new_data__isnull = False)
    print("\n書き換え予定の問題の数：%s" % updated_videos.count())

def videos():
    from .models import Video
    videos = Video.objects.filter(new_data__isnull = False)
    for i,video in enumerate(videos):
        print("\n\n%s:「%s」を更新中。。。" % (i,video))
        video.update()
        print(" 。。。更新成功")
    print("\n更新された問題の数：%s" % videos.count())


def playlists():
    from .models import Playlist
    playlists = Playlist.objects.all()
    # playlists = Playlist.objects.filter(data__snippet__description__icontains = "数列")#.exclude(data__snippet__title__icontains = "強化")
    for i,playlist in enumerate(playlists):
        print("\n\n%s:「%s」を更新中。。。" % (i,playlist))
        playlist.rewrite_title()
        print(playlist)
        playlist.update()
        # playlist.save()
    print("\n更新されたプレイリストの数：%s" % playlists.count())