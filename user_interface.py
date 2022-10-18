

import check as ch
import logger as log
import sys
import import_to_directory as im
import export
import json
import search as s

def main_menu():
    newxt_menu=ch.check_main_menu(input(f'Введите меню поля для дальнейшей работы:\n\t1: Просмотр справочника\n\t' +
                            '2: Импорт данных в справочник\n\t3: Экспорт данных из справочника\n\t4: Завершение и выход\n\t'))
    if newxt_menu == 4:
        print('Спасибо, что воспользовались нашим справочником')
        return sys.exit
    elif newxt_menu == 2:
        return import_menu()
    elif newxt_menu == 3:
        return export_menu()
    elif newxt_menu == 1:
        with open('Python/HW-PY_8/phone_number_directory.json', 'r') as read_json:
            print (read_json.read())
        main_menu()
   

def import_menu():
    newxt_menu=ch.check_import_menu(input(f'Меню Импорта выберите дальнейшее действие:\n\t1: Импорт в справочник из файла JSON \n\t'+
                            '2: Импорт в справочник из файла CSV\n\t3: Возврат в главное меню\n\t4: Завершение и выход\n\t'))
    
    if newxt_menu == 4:
        print('Спасибо, что воспользовались нашим справочником')
        return sys.exit
    elif newxt_menu == 3:
        return main_menu()
    elif newxt_menu == 1:
        im.import_to_directory(1)
        return import_menu()
    elif newxt_menu == 2:
        im.import_to_directory(2)
        return import_menu()

def export_menu():
    newxt_menu=ch.check_export_menu(input(f'Меню Экспорта выберите дальнейшее действие:\n\t1: Экспорт всего справочника в файл JSON \n\t'+
                                            '2: Экспорт всего справочника в файл CSV\n\t3: Экспорт справочника в файл JSON с применением фильтра\n\t'+
                                            '4: Экспорт справочника в файл CSV с применением фильтра\n\t5: Возврат в главное меню\n\t6: Завершение и выход\n\t'))
    data =s.search_records(1,'')
    if newxt_menu == 6:
        print('Спасибо, что воспользовались нашим справочником')
        return sys.exit
    elif newxt_menu == 5:
        return main_menu()
    elif newxt_menu == 1:
        export.export_data(data,1)
        return main_menu()
    elif newxt_menu == 2:
        export.export_data(data,2)
        return main_menu()
    elif newxt_menu == 3:
        search_field = ch.search_field_input(input(f'Введите идентификатор поля для задания фильтра:\n\t1: "Surname"\n\t'+
                                                    '2 : "Name"\n\t3 : "number"\n\t4 : "comments"\n\t'))
        element_for_search = input(f'Для поиска введите начало поля {search_field[1]}:')
        data =s.search_records(search_field[0],element_for_search)
        export.export_data(data,1)
        export_menu()
    elif newxt_menu == 4:
        search_field = ch.search_field_input(input(f'Введите идентификатор поля для задания фильтра:\n\t1: "Surname"\n\t'+
                                                    '2 : "Name"\n\t3 : "number"\n\t4 : "comments"\n\t'))
        element_for_search = input(f'Для поиска введите начало поля {search_field[1]}:')
        data =s.search_records(search_field[0],element_for_search)
        export.export_data(data,2)
        export_menu()

