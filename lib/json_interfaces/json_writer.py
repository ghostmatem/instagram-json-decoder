import json


class JsonFileWriter:
    def __init__(self, file_path):
        self._file_path = file_path

    def get_path(self):
        return self._file_path

    file_path = property(fget=get_path)

    def write(self, json_object):
        with open(self._file_path, "w") as write_file:
            json.dump(json_object, write_file)

    def read(self):
        try:
            with open(self._file_path, "r") as read_file:
                json_object = json.load(read_file)
            return json_object
        except:
            self.write(dict())
            return None

    def force_read(self):
        with open(self._file_path, "r") as read_file:
            json_object = json.load(read_file)
        return json_object


