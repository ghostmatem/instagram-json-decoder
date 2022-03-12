from pathlib import Path
from lib.data_handler.message_repository import MessageRepository
from lib.data_handler.message_provider import MessageProvider
from lib.utility_packages.message_printer import MessagePrinter


def get_path():
    return Path(Path.cwd(), 'data')


def main():
    provider = MessageProvider(get_path())
    repo = MessageRepository(provider)
    printer = MessagePrinter(repo)
    next_data = repo.load_next_data()
    counter = 0

    for _ in next_data:
        if counter == 0:
            printer.init_printed_file()
        printer.print_repository_data()
        counter += 1


main()
