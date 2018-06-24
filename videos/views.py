from django.http import JsonResponse
from django.views.generic import ListView, CreateView, DeleteView

from videos.models import Video, Vote


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
        super().form_valid(form)
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        super().form_invalid(form)
        return JsonResponse({'success': False})


class UnVoteView(DeleteView):

    model = Vote
    fields = ['video', ]

    def form_valid(self, form):
        super().form_valid(form)
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        super().form_invalid(form)
        return JsonResponse({'success': False})

