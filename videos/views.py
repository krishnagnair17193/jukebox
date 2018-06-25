from django.http import JsonResponse
from django.views.generic import ListView, CreateView, DeleteView

from videos.models import Video, Vote
from videos.templatetags.vote_utils import is_liked


class VideoListView(ListView):
    """
    Renders the listed video page
    """

    model = Video


class VoteView(CreateView):

    model = Vote
    fields = ['video', ]
    success_url = '/'

    def form_valid(self, form):
        if is_liked(self.request, form.cleaned_data.get('video').id):
            return JsonResponse({'success': False, 'message': 'This video is already liked'})
        obj = form.save(commit=False)
        obj.ip_address = self.request.META['REMOTE_ADDR']
        obj.save()
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        super().form_invalid(form)
        return JsonResponse({'success': False})


class UnVoteView(DeleteView):

    model = Vote

    def get_object(self, queryset=None):
        video_id = self.kwargs.get('video_id')
        return Vote.objects.get(video__id=video_id, ip_address=self.request.META['REMOTE_ADDR'])

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'success': True})
