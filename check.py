import os.path
import logger as log

def digit_check(input_value):
    while (input_value.isdigit() == False) or (int(input_value) < 1):
        input_value = input(f'Введите количество для генерации списка абонентов:\n\t')
        log.wrong_input(input_value)
    log.correct_input((input_value))
    return int(input_value)

def file_check(path):
    if os.path.exists(path):
        print(f'Прверка {path} пройдена успешно, продолжаем операцию')
        return True
    else:
        print(f'Прверка {path} не пройдена! Прверьте выполнение процедур формирования файла')
        return False

def search_field_input(menu_input):
    search_fields = {1: 'Surname', 2 : 'Name', 3 : 'number', 4 : 'comments'}
    while (menu_input.isdigit() == False) or (int(menu_input) < 1 or int(menu_input) >4):
        menu_input = input(f'Введите идентификатор поля для задания фильтра:\n{search_fields.items()}:\n\t')
        log.wrong_input(menu_input)
    menu_input = int(menu_input)
    log.correct_input(search_fields.get(menu_input))
    field_name = search_fields.get(menu_input)
    return menu_input, field_name
      
def check_main_menu(menu_value):
    main_menu_dic = {1: 'Просмотр справочника', 2: 'Импорт данных в справочник', 3: 'Экспорт данных из справочника', 4: 'Завершение и выход'}
    while (menu_value.isdigit() == False) or (int(menu_value) < 1 or int(menu_value) >4):
        menu_value = input(f'Введите меню поля для дальнейшей работы:\n{main_menu_dic.items()}:\n\t')
        log.wrong_input(menu_value)
    menu_value = int(menu_value)
    log.correct_input(main_menu_dic.get(menu_value))
    return menu_value

def check_import_menu(menu_value):
    main_menu_dic = {1: 'Импорт в справочник из файла JSON' , 2: 'Импорт в справочник из файла CSV' , 3: 'Возврат в главное меню', 4: 'Завершение и выход'}
    while (menu_value.isdigit() == False) or (int(menu_value) < 1 or int(menu_value) >4):
        menu_value = input(f'Введите меню поля для дальнейшей работы:\n{main_menu_dic.items()}:\n\t')
        log.wrong_input(menu_value)
    menu_value = int(menu_value)
    log.correct_input(main_menu_dic.get(menu_value))
    return menu_value 

def check_export_menu(menu_value):
    main_menu_dic = {1: 'Экспорт всего справочника в файл JSON', 
                    2: 'Экспорт всего справочника в файл CSV',
                    3: 'Экспорт справочника в файл JSON с применением фильтра',
                    4: 'Экспорт справочника в файл CSV с применением фильтра',
                    5: 'Возврат в главное меню',
                    6: 'Завершение и выход'}
    while (menu_value.isdigit() == False) or (int(menu_value) < 1 or int(menu_value) >6):
        menu_value = input(f'Введите меню поля для дальнейшей работы:\n{main_menu_dic.items()}:\n\t')
        log.wrong_input(menu_value)
    menu_value = int(menu_value)
    log.correct_input(main_menu_dic.get(menu_value))
    return menu_value 
