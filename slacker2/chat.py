import json

from slacker2 import BaseAPI


class Chat(BaseAPI):
    def post_message(self, channel, text=None, username=None, as_user=None,
                     parse=None, link_names=None, attachments=None,
                     unfurl_links=None, unfurl_media=None, icon_url=None,
                     icon_emoji=None, thread_ts=None, reply_broadcast=None,
                     blocks=None):
        attachments = json.dumps(attachments)
        blocks = json.dumps(blocks)
        return self.post('chat.postMessage',
                         data={
                             'channel': channel,
                             'text': text,
                             'username': username,
                             'as_user': as_user,
                             'parse': parse,
                             'link_names': link_names,
                             'attachments': attachments,
                             'unfurl_links': unfurl_links,
                             'unfurl_media': unfurl_media,
                             'icon_url': icon_url,
                             'icon_emoji': icon_emoji,
                             'thread_ts': thread_ts,
                             'reply_broadcast': reply_broadcast,
                             'blocks': blocks
                         })

    def me_message(self, channel, text):
        return self.post('chat.meMessage',
                         data={
                             'channel': channel,
                             'text': text
                         })

    def command(self, channel, command, text):
        return self.post('chat.command',
                         data={
                             'channel': channel,
                             'command': command,
                             'text': text
                         })

    def update(self, channel, ts, text, attachments=None, parse=None,
               link_names=False, as_user=None, blocks=None):
        attachments = json.dumps(attachments)
        blocks = json.dumps(blocks)
        return self.post('chat.update',
                         data={
                             'channel': channel,
                             'ts': ts,
                             'text': text,
                             'attachments': attachments,
                             'parse': parse,
                             'link_names': int(link_names),
                             'as_user': as_user,
                             'blocks': blocks
                         })

    def delete(self, channel, ts, as_user=False):
        return self.post('chat.delete',
                         data={
                             'channel': channel,
                             'ts': ts,
                             'as_user': as_user
                         })

    def post_ephemeral(self, channel, text, user, as_user=None,
                       attachments=None, link_names=None, parse=None,
                       blocks=None):
        attachments = json.dumps(attachments)
        blocks = json.dumps(blocks)
        return self.post('chat.postEphemeral',
                         data={
                             'channel': channel,
                             'text': text,
                             'user': user,
                             'as_user': as_user,
                             'attachments': attachments,
                             'link_names': link_names,
                             'parse': parse,
                             'blocks': blocks
                         })

    def unfurl(self, channel, ts, unfurls, user_auth_message=None,
               user_auth_required=False, user_auth_url=None):
        return self.post('chat.unfurl',
                         data={
                             'channel': channel,
                             'ts': ts,
                             'unfurls': unfurls,
                             'user_auth_message': user_auth_message,
                             'user_auth_required': user_auth_required,
                             'user_auth_url': user_auth_url,
                         })

    def get_permalink(self, channel, message_ts):
        return self.get('chat.getPermalink',
                        params={
                            'channel': channel,
                            'message_ts': message_ts
                        })
