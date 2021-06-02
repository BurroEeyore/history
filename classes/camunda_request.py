
class CamundaRequest:
    """Запрос за получением данных"""

    def get_last_definitions(self):
        """получаем последние версии всех развертываний"""
        pass

    def get_definitions_by_key(self):
        """получаем все развертывания по ключу"""
        pass

    def get_processes_by_definition(self):
        """получаем список процессов по развертыванию"""
        pass

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
