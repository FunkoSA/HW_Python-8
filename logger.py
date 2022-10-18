import datetime as dt
log_path = 'Python/HW-PY_8/dictionary_log.csv'
def abonents_generate_log(value):
    log_time = dt.datetime.now().strftime('%H:%M')
    with open(log_path,'a') as log:
        log.write ('\n {};Пользователь сгенерировал перечень абонентов для импорта; Файл:{}\n'.format(log_time, value))

def abonents_import_log(value):
    log_time = dt.datetime.now().strftime('%H:%M')
    with open(log_path,'a') as log:
        log.write ('\n {};Пользователь осуществил импорт абонентов в справочник из файла:{};\n'.format(log_time, value))

def abonents_export_log(value):
    log_time = dt.datetime.now().strftime('%H:%M')
    with open(log_path,'a') as log:
        log.write ('\n {};Пользователь осуществил экспорт абонентов из справочника; в файл: {}\n'.format(log_time, value))

def search_log(value1,value2):
    log_time = dt.datetime.now().strftime('%H:%M')
    with open(log_path,'a') as log:
        log.write ('\n {};Пользователь осуществил поиск записей из справочникапо полю: {} и значению: "{}";\n'.format(log_time, value1, value2))
def wrong_input (value):
    log_time = dt.datetime.now().strftime('%H:%M')
    with open(log_path,'a') as log:
        log.write ('\n {};Пользователь осуществил некорректный ввод: {}\n'.format(log_time, value))
def correct_input (value):
    log_time = dt.datetime.now().strftime('%H:%M')
    with open(log_path,'a') as log:
        log.write ('\n {};Переход к следующей операции: {}\n'.format(log_time, value))
