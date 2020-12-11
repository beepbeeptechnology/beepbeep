# beepbeep.ss: spreadsheet functions
import csv
from xlrd import open_workbook


def convert_local_excel_file_sheet_to_dict(local_excel_file_path, sheet_name, start_row=0, start_col=0, on_demand=True):
    try:
        workbook = open_workbook(local_excel_file_path) 
        sheet_names = workbook.sheet_names()

        sheet = workbook.sheet_by_name(sheet_name)
        sheet_headers = dict( (i, sheet.cell_value(start_col, i) ) for i in range(sheet.ncols) ) 
        output_generator = (dict( (sheet_headers[j], sheet.cell_value(i, j)) for j in sheet_headers ) for i in range(start_row + 1, sheet.nrows) )

        output_dict = [row for row in output_generator]

    except Exception as e:
        print(e)
        output_dict = None

    return output_dict


def write_list_of_dicts_to_csv(input_dict_list, output_filename):
    csv_columns = input_dict_list[0].keys()

    try:
        with open(output_filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile,delimiter=',', fieldnames=csv_columns)
            writer.writeheader()
            for data in input_dict_list:
                writer.writerow(data)
    
    except Exception as e:
        print(e)
        csvfile = None
    
    return csvfile