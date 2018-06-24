import re

from django.db import models


class VideoManager(models.Manager):
    """
    Custom manager to always order video based on the number of counts
    """
    def get_queryset(self):
        return super(VideoManager, self).get_queryset().\
            annotate(votes=models.Count('get_all_votes')).order_by('-votes')


class Video(models.Model):
    """
    Used to store the details of the youtube links posted in the configured workspace and channel
    """

    url = models.URLField()
    title = models.CharField(max_length=255, null=True)
    thumb_url = models.URLField(null=True)
    extra_details = models.TextField(null=True)

    objects = VideoManager()

    def __str__(self):
        return self.url

    def video_id(self):
        match = re.search(r"youtube\.com/.*v=([^&]*)", self.url)
        if match:
            return match.group(1)
        return ''


class Vote(models.Model):

    """
    Used to save the votes obtained for the videos
    """

    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='get_all_votes')
    created = models.DateTimeField(auto_now_add=True)

    # TODO Add fields to restrict voting based on user or IP

    def __str__(self):
        return self.video.url
