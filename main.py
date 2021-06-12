from classes.dialog import Dialog
from text_templates import FIRST_MSG

if __name__ == '__main__':
    print(FIRST_MSG)
    dialog = Dialog()
    dialog.set_environment()
    dialog.set_camunda_type()
    print('hello')
# создать диалог с выводом результатов как есть
# сделать печать результатов в читаемом виде
