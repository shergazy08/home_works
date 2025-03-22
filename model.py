# def last_sum(a,b):
#     return a+b
#
#
# def last_sum(a,b):
#     return a-b


a = {
    'ru': 'Привет',
    'en': 'Hello',
    'es': 'Hola',
    'fr': 'Bonjour',
    'de': 'Hallo',
    'it': 'Ciao',
    'zh': '你好',
    'ja': 'こんにちは'
}

def great(lang):
    if lang in a:
        return lang[a]
    else:
        return 'myndai gok'




user_data = []


def add_user(username):
    user_data.append(username)
    return f'Пользователь {username} добавлен'


def get_user():
    return user_data


def delete_user(username):
    if username in user_data:
        user_data.remove(username)
        return f'Пользователь {username} удален'
    else:
        return f'Пользователь {username} не найден'

