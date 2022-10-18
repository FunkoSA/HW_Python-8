import csv
import json
import random

 
surname = []
with open('Python/HW-PY_8/russian_surnames2.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        surname.append(row)
#    print (results)

female_surnam = []
for surname_list in surname:
    
    if surname_list['Surname'] [-1] not in 'ая':
        
        
        female_surnam.append(surname_list)
print (female_surnam)
# for surname_list in results:
#     if surname_list['Surname'] [-1] in 'ая':
        #surname_list ['Sex'] = 'Ж'
        # print (surname_list['Surname'],surname_list['Sex'])
        # print (surname_list)

#print (random.choice(results))

for j in range (0,20):
    telefon_number = '+7'
    for i in range (0,10):
        telefon_number += str(random.randint(0,9))
    abonent = random.choice(surname)

    print (j,abonent['Surname'],abonent['Sex'],telefon_number)
    print (abonent)

# with open('Python/HW-PY_8/male_surnames.csv', 'w') as csvfile:
#     fieldnames = ['ID', 'Surname', 'Sex']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(female_surnam)
 
# print("Writing complete")

# for surname, sex in results:
#     print (surname, sex)
   
   
    # if surname[-1] in 'а':
    #     sex = 'Ж'

