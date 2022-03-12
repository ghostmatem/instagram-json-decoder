from lib.data_handler.message_repository import MessageRepository
from lib.entity.message import *
from lib.data_handler.file_delegate import FileDelegate
from pathlib import Path
import lib.utility_packages.content_format as content_format
import lib.utility_packages.time_format as time_format
from datetime import datetime


class MessagePrinter:
    def __init__(self, message_repository: MessageRepository):
        self._message_repository = message_repository
        self._file_delegate = None

    def init_printed_file(self):
        path = Path(' - '.join(self._message_repository.names)+'.txt')
        self._file_delegate = FileDelegate(path, encoding='utf-8')
        self._file_delegate.check_and_create_file()

    def print_repository_data(self):
        if self._file_delegate is None:
            return

        current_user = ''
        current_data = datetime(1970, 1, 1)
        date_border = ' ' + '-'*40 + ' '
        name_border = ' ' + '-'*30 + ' '
        self._print_current_package(current_user, current_data, date_border, name_border)

    def _print_current_package(self, current_user, current_data, date_border, name_border):
        path = self._file_delegate.path
        encoding = self._file_delegate.encoding
        file = open(path, 'a', encoding=encoding)
        for message in self._message_repository.messages:

            if not time_format.is_equals_data(current_data, message.time):
                current_data = message.time
                current_user = ''
                result_str = '\n'*4 + date_border \
                             + time_format.get_str_full_time(current_data) + date_border + '\n'
                file.write(result_str)

            if current_user != message.sender_name:
                current_user = message.sender_name
                file.write('\n' + name_border + current_user + name_border + '\n')

            file.write('\n')
            self._print_message(message, file)
        file.close()

    def _print_message(self, message: Message, file):
        str_time = time_format.get_time_of_day_str(message.time)
        file.write(' ' + str_time + ': ')
        self._try_print_str(message.content.text, file)
        self._try_print_list_attribute(message.content.photo, file, 'Вложенные фото: ')
        self._try_print_list_attribute(message.content.audio, file, 'Вложенные аудио: ')
        self._try_print_str(message.content.share, file, 'Вложенная ссылка: ')

    def _try_print_str(self, string, file, title='', end='\n'):
        if string is None:
            return False
        file.write(title + content_format.from_iso(string) + end)

    def _try_print_list_attribute(self, attribute: list, file, title='', title_sep='\n', attribute_sep='\n', ):
        if attribute is None:
            return False
        file.write(title + title_sep)
        for string in attribute:
            file.write(string + attribute_sep)
        return True