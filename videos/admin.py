from django.contrib import admin

from videos.models import Video, Vote

admin.site.register(Video)
admin.site.register(Vote)
