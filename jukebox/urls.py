"""jukebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.contrib import admin
from django.urls import path
from slack import views as slack_views
from videos.views import VideoListView, VoteView, UnVoteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('incoming/', slack_views.incoming_message, name="incoming_message_hook"),
    path('', VideoListView.as_view(), name="video_list"),
    path('vote/', VoteView.as_view(), name="vote"),
    path('unvote/<int:video_id>/', UnVoteView.as_view(), name="unvote"),
]
