import json

import requests

from settings import ACCESS_URLS
from tools import get_token


class CamundaRequest:
    """Запрос за получением данных"""
    def __init__(self, env, camunda_type):
        self.env = env
        self.camunda_type = camunda_type
        self.base_url = '{0}{1}{2}'.format(
            ACCESS_URLS.get(self.env).get('camunda_url'),
            self.camunda_type,
            '/api/engine/engine/default/'
        )

    def get_last_definitions(self):
        """получаем последние версии всех развертываний"""
        url = '{0}{1}'.format(
            self.base_url,
            'process-definition?latestVersion=true&sortBy=key&sortOrder=asc',
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
        """
        получаем все развертывания по ключу
        :param key: ключ развертывания
        """
        url = '{0}{1}'.format(
            self.base_url,
            'process-definition?key={0}&sortBy=version&sortOrder=desc'.format(key),
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

    def get_process_by_key(self, key):
        """
        получаем все процессы по бизнес-ключу
        :param key: бизнес-ключ или его фрагмент
        """
        url = '{0}{1}'.format(
            self.base_url,
            'process-instance?businessKeyLike={}'.format(key),
        )
        headers = {
            'Accept': 'application/json',
            'Authorization': get_token(self.env)
        }
        resp = requests.get(url=url, headers=headers)
        if resp.status_code != 200:
            print('Поиск процесса по бизнес-ключу: код ответа не равен 200!')
            return []
        else:
            return json.loads(resp.content)

    def get_processes_by_definition(self, deployment_id):
        """
        получаем список ЗАВЕРШЕННЫХ процессов по развертыванию
        :param deployment_id: идентификатор развертывания
        """
        url = '{0}{1}'.format(
            self.base_url,
            'history/process-instance',
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

    def get_process_variables(self, process_id):
        """
        получаем список переменных по идентификатору процесса
        :param process_id: идентификатор процесса
        """
        url = '{0}{1}'.format(
            self.base_url,
            'history/variable-instance',
        )
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': get_token(self.env)
        }
        body = {
            "processInstanceId": process_id,
            "sorting": [
                {
                  "sortBy": "variableName",
                  "sortOrder": "asc"
                },
                {
                  "sortBy": "instanceId",
                  "sortOrder": "desc"
                }
              ]
            }
        resp = requests.post(url=url, headers=headers, json=body)
        if resp.status_code != 200:
            print('Запрос переменных процесса: код ответа не равен 200!')
            return []
        else:
            return json.loads(resp.content)

    def get_variable(self, variable_id, deserialize=True):
        """
        получаем значение переменной с/без десериализацией
        :param variable_id: идентификатор переменной
        :param deserialize: флаг необходимости десериализации (требуется для объектов)
        """
        url = '{0}{1}'.format(
            self.base_url,
            'history/variable-instance/{0}?deserializeValue={1}'.format(
                variable_id,
                'true' if deserialize else 'false'
            )
        )
        headers = {
            'Accept': 'application/json',
            'Authorization': get_token(self.env)
        }
        resp = requests.get(url=url, headers=headers)
        if resp.status_code != 200:
            print('Запрос значения переменной: код ответа не равен 200!')
            return []
        else:
            return json.loads(resp.content)

    def get_incidents_by_process(self, process_id):
        """
        получаем историю инцидентов по processInstanceId
        :param process_id: идентификатор процесса
        """
        url = '{0}{1}'.format(
            self.base_url,
            'history/incident?processInstanceId={0}'.format(process_id)
        )
        headers = {
            'Accept': 'application/json',
            'Authorization': get_token(self.env)
        }
        resp = requests.get(url=url, headers=headers)
        if resp.status_code != 200:
            print('Запрос истории инцидентов: код ответа не равен 200!')
            return []
        else:
            return json.loads(resp.content)
