import os
from lib.json_interfaces.json_writer import JsonFileWriter
from lib.entity.message import Message


class MessageProvider:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self._files = self._get_directories()
        self.files_length = len(self._files)

    def _get_directories(self):
        dir_files = os.listdir(self.directory_path)
        full_paths = map(lambda name: os.path.join(self.directory_path, name), dir_files)
        files = []
        for file in full_paths:
            if os.path.isfile(file):
                files.append(file)
            files.sort()
        return files

    def get_messages_package(self, index):
        if not 0 <= index < self.files_length:
            raise Exception('Индекс вышел за пределы')

        json_writer = JsonFileWriter(self._files[index])
        result = json_writer.read()
        return MessageProvider._from_json(result)

    @staticmethod
    def _from_json(json_object):
        names = [obj['name'] for obj in json_object.get('participants', {})]
        messages = [Message.from_json(message) for message in json_object.get('messages', [])]
        return names, messages
