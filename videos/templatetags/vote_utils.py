from django import template

from videos.models import Vote

register = template.Library()


@register.simple_tag
def is_liked(request, video):
    if Vote.objects.filter(
            ip_address=request.META['REMOTE_ADDR'],
            video__id=video,
    ).exists():
        return True
    return False
