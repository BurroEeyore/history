from colorama import init, Fore


class Printer:
    """Отображение информации"""

    def print_table(self):
        """Отображение результатов в виде таблицы"""
        pass

    @staticmethod
    def print_ask(ask, answer=''):
        """Отображение вопросов"""
        init(autoreset=True)
        print(Fore.GREEN + ask)
        print(answer)
        return
