import json
import logger as log

def search_records(field,search_value):
    search_fields = {1: 'Surname', 2 : 'Name', 3 : 'number', 4 : 'comments'}
    field = search_fields.get(field)
    with open('Python/HW-PY_8/phone_number_directory.json', 'r') as read_json:
        data = json.load(read_json)
    view_elements =[]
    if len(search_value) ==0:
        for elements in data['phone_numbers']:
            view_elements.append(elements)
    else:
        for elements in data['phone_numbers']:
            if elements[field] [:len(search_value)].lower() == search_value.lower():
                view_elements.append(elements)
    search_data = json.dumps(view_elements, ensure_ascii=False, indent=2)
    log.search_log(field,search_value)
    return search_data


