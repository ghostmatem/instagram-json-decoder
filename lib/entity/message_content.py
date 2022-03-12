from lib.json_interfaces.i_serializable import ISerializable
import lib.utility_packages.content_format as format


class MessageContent(ISerializable):
    def __init__(self, text: str | None, photo: list | None, audio: list | None, share: str | None):
        self.text = text
        self.photo = photo
        self.audio = audio
        self.share = share

    @staticmethod
    def from_json(json_object):
        content = json_object.get('content', None)
        photo = json_object.get('photos', None)
        audio = json_object.get('audio_files', None)
        share = json_object.get('share', {}).get('link', None)
        return MessageContent(
            content,
            photo=format.get_list_at_key(photo, 'uri'),
            audio=format.get_list_at_key(audio, 'uri'),
            share=share
        )
