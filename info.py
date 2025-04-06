#Alex Anderson, file that converts,saves, and loads info from csv

import csv

# function that reads the data and returns it as a list
def read_info():
    with open("info.csv", "r") as file:
        reader = csv.reader(file)
        row = next(reader)
        return row

# function that writes the updated data back into info.csv
def save_info(row):
    with open("info.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)

# function to safely read the csv file and return data
def safe_read_info():
    try:
        return read_info()
    except Exception as e:
        print("Error reading info.csv:", e)
        return ["", "", "[]", "[]"]

# function to convert a string to a list of dictionaries
def string_to_list_of_dicts(s):
    s = s.strip()[1:-1]
    items = s.split('},')
    result = []
    
    for item in items:
        item = item.strip().strip('{}') 
        if item:
            kv_pairs = item.split(',')  #split by commas between pairs
            d = {}
            for pair in kv_pairs:
                key, value = pair.split(':')
                d[key.strip().strip('"')] = value.strip().strip('"')
            result.append(d)
    
    return result

# function to convert a list of dictionaries to a string
def list_of_dicts_to_string(lst):
    result = "["
    for d in lst:
        result += "{"
        for key, value in d.items():
            result += f'"{key}": "{value}", '
        result = result.rstrip(', ')
        result += "}, "
    result = result.rstrip(', ')
    result += "]"
    return result