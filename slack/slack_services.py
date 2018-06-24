

class SlackService(object):
    """
    Contains methods that helps in identifying relevant links shared in the channel and process it
    """

    def check_for_message(self, request_body):
        """

        :param request_body: the body of request obtained from slack
        :return: True or False evaluating
        """
        event = request_body.get('event')
        if event and event.get('message'):
            return True
        return False

    def retrieve_data(self, message):
        attachments = message.get('attachments')
        if attachments:
            return [
                {'url': attachment.pop('original_url'),
                 'title': attachment.pop('title'),
                 'thumb_url': attachment.pop('thumb_url'),
                 'extra_details': attachment,
                 } for attachment in attachments]
        return []

    def validate_links(self, links):
        return [link for link in links if 'youtube.com' in link.get('url')]
