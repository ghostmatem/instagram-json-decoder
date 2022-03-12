from datetime import datetime


mounths = (
    'Января',
    'Февраля',
    'Марта',
    'Апреля',
    'Мая',
    'Июня',
    'Июля',
    'Августа',
    'Сентября',
    'Октября',
    'Ноября',
    'Декабря',
)


def get_time_from_time_stamp(time_stamp):
    return datetime.utcfromtimestamp(time_stamp / 1000)


def get_time_of_day_str(time: datetime):
    return get_str_time_element(time.hour) + ':' + get_str_time_element(time.minute)


def get_str_time_element(num):
    str_num = str(num)
    if num // 10 == 0:
        return '0' + str_num
    return str_num


def get_str_full_time(time: datetime):
    return f'{time.day} {mounths[time.month - 1]} {time.year} г.'


def is_equals_data(first: datetime, second: datetime):
    return first.day == second.day and first.month == second.month and first.year == second.year
