import json
import sys

import requests

from settings import *


def get_token(env):
    """Получение авторизационного ключа для включения в заголовки запроса
    :param env: Окружение
    """

    if env not in ACCESS_URLS.keys():
        print('Не найден URL для указанного окружения. Доступные значения: dev, test, stage')
        return

    url = ACCESS_URLS.get(env).get('access_url')

    payload = ACCESS_PAYLOAD
    headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

    res = requests.post(url, data=payload, headers=headers)
    execution = json.loads(res.content)['execution']

    add_payload = {
        '_eventId': 'next',
        'username': ACCESS_USERNAME,
        'password': ACCESS_PASSWORD,
        'execution': execution
    }

    res = requests.post(url, data={**payload, **add_payload}, headers=headers)
    token = 'Bearer sso_1.0_' + json.loads(res.content)['access_token']
    return token


