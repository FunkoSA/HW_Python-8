import json
import csv
import logger as log
import check as ch
import abonents as ab



def import_to_directory(import_type):

    directoty_path = 'Python/HW-PY_8/phone_number_directory.json'
    data = json.load(open(directoty_path))
    
    if import_type == 1:
        import_path ='Python/HW-PY_8/for_import/abonents.json'
        if ch.file_check(import_path):
            data_for_import = json.load(open(import_path))
            for data_imrort in data_for_import['phone_number']:
                data['phone_numbers'].append(data_imrort)
        else:
            ab.get_abonent(ch.digit_check(input(f'Отсутствует фал для иморта\n\tВведите количество для генерации списка абонентов:\n\t')),1)
            import_to_directory(1)
    else:
        import_path='Python/HW-PY_8/for_import/abonents.csv'
        if ch.file_check(import_path):
            with open(import_path) as file:
                data_for_import = csv.DictReader(file)
                for data_imrort in data_for_import:
                    data['phone_numbers'].append(data_imrort)
        else:
            ab.get_abonent(ch.digit_check(input(f'Отсутствует фал для иморта\n\tВведите количество для генерации списка абонентов:\n\t')),2)
            import_to_directory(2)
    with open(directoty_path, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    log.abonents_import_log(import_path)
    print ('Выполнен импорт')


