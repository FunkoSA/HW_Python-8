import json
import csv
import datetime as dt
import logger as log


def export_data(data_for_export, export_type):
    export_date_time = dt.datetime.now().strftime('%Y.%M.%d_%H:%M:%S')
    if export_type ==1:
        export_path = 'Python/HW-PY_8/exported/export_dictionary'+export_date_time+'.json'
        with open(export_path, 'w') as write_json:
            write_json.write(data_for_export) 
        
    else:
        export_path = 'Python/HW-PY_8/exported/export_dictionary'+export_date_time+'.csv'
        data_for_export = json.loads(data_for_export)
        with open(export_path, 'w') as csv_f:
            csv_writer = csv.writer(csv_f)
            count = 0
            for data in data_for_export:
                if count == 0:
                    # Writing headers of CSV file
                    header = data.keys()
                    csv_writer.writerow(header)
                    count += 1
                # Writing data of CSV file
                csv_writer.writerow(data.values())
    log.abonents_export_log(export_path)
