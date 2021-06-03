import json

import requests

from settings import ACCESS_URLS
from tools import get_token


class CamundaRequest:
    """Запрос за получением данных"""
    def __init__(self, env, camunda_type):
        self.env = env
        self.camunda_type = camunda_type

    def get_last_definitions(self):
        """получаем последние версии всех развертываний
        """
        url = '{0}{1}{2}'.format(
            ACCESS_URLS.get(self.env).get('camunda_url'),
            self.camunda_type,
            '/api/engine/engine/default/process-definition?latestVersion=true&sortBy=key&sortOrder=asc',
        )
        headers = {
            'Accept': 'application/json',
            'Authorization': get_token(self.env)
        }
        resp = requests.get(url=url, headers=headers)
        if resp.status_code != 200:
            print('Запрос последних версий развертываний: код ответа не равен 200!')
            return []
        else:
            return json.loads(resp.content)

    def get_definitions_by_key(self, key):
        """получаем все развертывания по ключу"""
        url = '{0}{1}{2}'.format(
            ACCESS_URLS.get(self.env).get('camunda_url'),
            self.camunda_type,
            '/api/engine/engine/default/process-definition?key={}&sortBy=version&sortOrder=desc'.format(key),
        )
        headers = {
            'Accept': 'application/json',
            'Authorization': get_token(self.env)
        }
        resp = requests.get(url=url, headers=headers)
        if resp.status_code != 200:
            print('Запрос развертывания по ключу: код ответа не равен 200!')
            return []
        else:
            return json.loads(resp.content)

    def get_processes_by_definition(self, deployment_id):
        """получаем список ЗАВЕРШЕННЫХ процессов по развертыванию"""
        url = '{0}{1}{2}'.format(
            ACCESS_URLS.get(self.env).get('camunda_url'),
            self.camunda_type,
            '/api/engine/engine/default/history/process-instance',
        )
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': get_token(self.env)
        }
        body = {
            'processDefinitionId': deployment_id,
            'finished': True,
            'sorting': [
                {
                    'sortBy': 'businessKey',
                    'sortOrder': 'desc'
                },
                {
                    'sortBy': 'startTime',
                    'sortOrder': 'desc'
                }
            ]
        }
        resp = requests.post(url=url, headers=headers, json=body)
        if resp.status_code != 200:
            print('Запрос завершенных процессов: код ответа не равен 200!')
            return []
        else:
            return json.loads(resp.content)

    def get_process_variables(self):
        """получаем переменные по идентификатору процесса"""
        pass

    def get_deserialize_variable(self):
        """получаем конкретную переменную с сериализацией"""
        pass

    def get_not_deserialize_variable(self):
        """получаем конкретную переменную без сериализации"""
        pass

    def get_incidents_by_process(self):
        """получаем историю инцидентов по processInstanceId"""
        pass
