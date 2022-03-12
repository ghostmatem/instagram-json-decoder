from pathlib import Path


class FileDelegate:
    def __init__(self, relative_path: Path, encoding: str | None):
        self._path = Path(Path.cwd(), relative_path)
        self._file_exist = self.check_file()
        self._file_encoding = encoding

    def get_file_exist(self):
        return self._file_exist

    def get_encoding(self):
        return self._file_encoding

    file_exist = property(fget=get_file_exist)
    encoding = property(fget=get_encoding)

    def check_and_create_file(self):
        """Создать файл, если он отсутствует"""
        self._file_exist = self.check_file()
        if not self._file_exist:
            self._file_exist = self.create_file()
        return self._file_exist

    def get_path(self):
        return self._path

    path = property(fget=get_path)

    def create_file(self):
        try:
            if self._file_encoding is None:
                file = open(self._path, 'w')
                file.close()
            else:
                file = open(self._path, 'w', encoding=self._file_encoding)
                file.close()
            return True
        except:
            return False

    def check_file(self):
        try:
            if self._file_encoding is None:
                file = open(self._path, 'r')
                file.close()
            else:
                file = open(self._path, 'r', encoding=self._file_encoding)
                file.close()
            return True
        except:
            return False
