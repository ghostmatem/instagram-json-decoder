from lib.json_interfaces.i_serializable import ISerializable
from lib.entity.message_content import MessageContent
import lib.utility_packages.time_format as time_format
from datetime import datetime


class Message(ISerializable):
    def __init__(self, sender_name: str, content: MessageContent, time: datetime):
        self.sender_name = sender_name
        self.content = content
        self.time = time

    @staticmethod
    def from_json(json_object: dict):
        return Message(
            sender_name=json_object['sender_name'],
            time=time_format.get_time_from_time_stamp(json_object['timestamp_ms']),
            content=MessageContent.from_json(json_object),
        )
