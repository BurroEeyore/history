from colorama import init, Fore

from settings import ACCESS_URLS, CAMUNDA_TYPES


class Dialog:
    """Диалог с пользователем"""
    def __init__(self):
        self.env = ''
        self.camunda_type = ''
        self.business_key = ''

    def set_environment(self):
        """установка окружения"""
        envs = ACCESS_URLS.keys()
        init(autoreset=True)
        response = self.env
        while response not in envs:
            print(Fore.GREEN + 'Выберите окружение из предложенного списка:')
            print('\n'.join([env for env in envs]))
            response = input()

        self.env = response
        print('Окружение: {}\n'.format(self.env))
        return self.env

    def set_camunda_type(self):
        """установка экземпляра камунды"""
        types = CAMUNDA_TYPES
        init(autoreset=True)
        response = self.camunda_type
        while response not in types:
            print(Fore.GREEN + 'Выберите экземпляр камунды из предложенного списка:')
            print('\n'.join([env for env in types]))
            response = input()

        self.camunda_type = response
        print('Камунда: {}\n'.format(self.camunda_type))
        return self.camunda_type

    def set_business_key(self):
        """установить бизнес-ключ"""
        response = self.business_key
        while response == '':
            print(Fore.GREEN + 'Укажите номер заявки(бизнес-ключ):')
            response = input()
        self.business_key = response
        print('Номер заявления: {}\n'.format(self.business_key))

        return self.business_key

    # запрос переменных процесса
    # запрос переменной
    # запрос инцидентов (запрос отдельного инцидента?)
