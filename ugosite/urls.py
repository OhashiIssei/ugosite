from django.urls import path
from . import views

import youtube

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
]

urlpatterns += [
    path('term/<int:pk>', views.TermDetailView.as_view(), name='term-detail'),
    path('terms/', views.TermListView.as_view(), name='terms'),
]

urlpatterns += [
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('categorys/', views.CategoryListView.as_view(), name='categorys'),
]

urlpatterns += [
    path('problem/<int:pk>', views.ProblemDetailView.as_view(), name='problem-detail'),
    path('problems/', views.ProblemListView.as_view(), name='problems'),
]

urlpatterns += [
    # path('randomvideo/', youtube.views.VideoOnAppListView.as_view(), name='random_video'),
    path('video_search/<int:pk>', youtube.views.VideoSearchView.as_view(), name='video_search'),
    path('video/<int:pk>', youtube.views.VideoOnAppDetailView.as_view(), name='video-detail'),
]





