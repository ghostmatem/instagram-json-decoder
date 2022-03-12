from lib.data_handler.message_provider import MessageProvider


class MessageRepository:
    def __init__(self, provider: MessageProvider):
        self._provider = provider
        self.names = []
        self.messages = []

    def load_next_data(self):
        for index in range(self._provider.files_length):
            names, messages = self._provider.get_messages_package(index)

            if names != self.names and len(names) > 0:
                self.names = names

            self.messages = messages
            yield
