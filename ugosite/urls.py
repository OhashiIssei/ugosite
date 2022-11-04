from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('genre/<slug:slug>', views.GenreDetailView.as_view(), name='genre-detail'),
    path('genres/', views.GenreListView.as_view(), name='genres'),
]

urlpatterns += [
    path('article/<slug:slug>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
]

urlpatterns += [
    path('term/<slug:slug>', views.TermDetailView.as_view(), name='term-detail'),
    path('terms/', views.TermListView.as_view(), name='terms'),
]

urlpatterns += [
    path('module/<slug:slug>', views.ModuleDetailView.as_view(), name='module-detail'),
    path('modules/', views.ModuleListView.as_view(), name='modules'),
]

urlpatterns += [
    path('problem/<slug:slug>', views.ProblemDetailView.as_view(), name='problem-detail'),
    path('problems/', views.ProblemListView.as_view(), name='problems'),
    path('problem/<slug:slug>/edit/', views.problemEditView, name='problem-edit'),
]

urlpatterns += [
    path('video/<slug:slug>/', views.VideoDetailView.as_view(), name='video-detail'),
    path('video/<slug:slug>/update/', views.VideoUpdate.as_view(), name='video-update'),
    path('videos/', views.VideoListView.as_view(), name='videos'),
]

urlpatterns += [
    path('playlist/<slug:slug>/',views.PlaylistDetailView.as_view(), name='playlist-detail'),
    path('playlists/', views.PlaylistListView.as_view(), name='playlists'),
]

urlpatterns += [
    path('article/<int:pk>/comment/', views.CommentCreate.as_view(), name='comment-create'),
    path('comment/<pk>/update/', views.CommentUpdate.as_view(), name='comment-update'),
    path('comment/<pk>/delete/', views.CommentDelete.as_view(), name='comment-delete'),
]

urlpatterns += [
    path('accounts/create/', views.UserCreate.as_view() ,name = 'account_create'),
]

urlpatterns += [
    path('profile/', views.profileView ,name = 'profile'),
    # path('notes/<pk>', views.notesView ,name = 'notes'),
]


urlpatterns += [
    path('note/<pk>/', views.NoteDetailView.as_view(), name='note-detail'),
    path('notes/', views.NoteListView.as_view(), name='notes'),
]

urlpatterns += [
    path('folder/<pk>/', views.FolderDetailView.as_view(), name='folder-detail'),
    path('folders/', views.FolderListView.as_view(), name='folders'),
]