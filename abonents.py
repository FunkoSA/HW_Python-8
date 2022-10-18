import csv
import json
import random
import logger as log

def get_abonent(amount,file_type):
    '''Генерация файлов для импорта контактов 1 - JSON, 2 - CSV'''
    comment =['Рабочий','Домашний','Личный','Для коммандировок','Для поездок за границу'] 
    male_surnames = []
    with open('Python/HW-PY_8/for_abbs_generate/male_surnames.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            male_surnames.append(row)
            
    female_surnames = []
    with open('Python/HW-PY_8/for_abbs_generate/female_surnames.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            female_surnames.append(row)

    with open('Python/HW-PY_8/for_abbs_generate/new_names.json', 'r') as read_json:
        names = json.load(read_json)

    if file_type == 1:
        file_path ='Python/HW-PY_8/for_import/abonents.json'
        new_abonent ={}
        new_abonent['phone_number'] = []
        for j in range (0,amount):
            telefon_number = '+7'
            for i in range (0,10):
                telefon_number += str(random.randint(0,9))
            abonent_name = random.choice(names['names'])
            if abonent_name['Sex'] == 'Ж':
                abonent_surnames = random.choice(female_surnames)
            else:
                abonent_surnames = random.choice(male_surnames)
            comments = random.choice(comment)
            new_abonent['phone_number'].append({'Surname': abonent_surnames['Surname'] , 'Name' : abonent_name['Name'] , 'number': telefon_number , 'comments' : comments})
        data = json.dumps(new_abonent,ensure_ascii=False, indent=2)
        with open(file_path, 'w') as write_json:
            write_json.write(data) 
    else:
        file_path ='Python/HW-PY_8/for_import/abonents.csv'
        new_abonent = []
        for j in range (0,amount):
            telefon_number = '+7'
            for i in range (0,10):
                telefon_number += str(random.randint(0,9))
            abonent_name = random.choice(names['names'])
            if abonent_name['Sex'] == 'Ж':
                abonent_surnames = random.choice(female_surnames)
            else:
                abonent_surnames = random.choice(male_surnames)
            comments = random.choice(comment)
            new_abonent.append({'Surname': abonent_surnames['Surname'] , 'Name' : abonent_name['Name'] , 'number': telefon_number , 'comments' : comments})
        with open(file_path, 'w') as csvfile:
            fieldnames = ['Surname', 'Name', 'number','comments']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(new_abonent)
    log.abonents_generate_log(file_path)






# comments =['Рабочий','Домашний','Личный','Для коммандировок','Для поездок за границу'] 
# for i in range (0,10):
#     print(random.choice(comments))