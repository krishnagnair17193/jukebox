import json

from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from slack.slack_services import SlackService
from videos.models import Video


@csrf_exempt
def incoming_message(request):
    """
    View to receive the webhook request from slack and check for the youtube link.
    If relevant link is incoming, save the data to DB
    :param request:
    :return: Response to slack events API, 200 status and the challenge code from the request in body
    """
    request_body = json.loads(request.body.decode('utf8'))
    validate_service = SlackService()
    if validate_service.check_for_message(request_body):
        message = request_body.get('event').get('message')
        links = validate_service.retrieve_data(message)
        relevant_data = validate_service.validate_links(links)
        relevant_link_objs = [Video(**link) for link in relevant_data if Video.objects.filter(**link).count() < 1]
        Video.objects.bulk_create(relevant_link_objs)
    return HttpResponse(status=200, content_type='text/plain')
