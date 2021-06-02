from classes.printer import Printer
from settings import ACCESS_URLS
from text_templates import FIRST_MSG, ENV_MSG

if __name__ == '__main__':
    print(FIRST_MSG)
    printer = Printer
    text_envs = '\n'.join([env for env in ACCESS_URLS.keys()])
    printer.print_ask(ask=ENV_MSG, answer=text_envs)

