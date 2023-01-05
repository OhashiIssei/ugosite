

MY_CHANNEL_ID = "UCtEVdDYltR4eWf-QXvjmCJQ"

def playlists():
    from .models import Channel,Playlist
    Playlist.objects.all().delete()
    cannel = Channel(channelId = MY_CHANNEL_ID)
    cannel.download_playlists()

def playlistItems():
    from .models import Playlist,PlaylistItem
    PlaylistItem.objects.all().delete()
    playlists = Playlist.objects.all()
    for playlist in playlists:
        playlist.download_playlistItems()

def videos():
    from .models import Channel,Video
    cannel = Channel(channelId = MY_CHANNEL_ID)
    playlistItems = cannel.download_uploads_playlistItems()
    for playlistItem in playlistItems:
        playlistItem.download_video()

def sections():
    from .models import Channel,ChannelSection
    ChannelSection.objects.all().delete()
    cannel = Channel(channelId = MY_CHANNEL_ID)
    cannel.download_sections()