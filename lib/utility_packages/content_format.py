def parse_content_json(json_object: dict):
    content = '\t' + json_object.get('content', '')
    photo = json_object.get('photos', None)
    audio = json_object.get('audio_files', None)

    if photo is None and audio is None:
        return content

    content_str = content + '\n\n'
    photo_str = get_part(photo, 'Вложенные фото:', message_sep='\n\t\t')
    audio_str = get_part(audio, 'Вложенные аудио:', message_sep='\n\t\t')

    return content_str + photo_str + audio_str


def get_part(ls, title: str, title_sep='\n\n', message_sep='\n\n'):
    if ls is None:
        return ''
    message = get_uri_message(ls, message_sep)
    return title + title_sep + message


def get_list_at_key(object_list: list, key):
    if object_list is None:
        return None

    return [obj[key] for obj in object_list]


def from_iso(text: str):
    try:
        return bytes(text, 'iso-8859-1').decode('utf-8')
    except:
        return text
