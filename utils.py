#Alex Anderson, file that converts,saves, and loads info from csv

import csv

def read_info():
    with open("info.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        return [row for row in reader]  # Return all rows as a list of lists

def save_info(data):
    with open("info.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)  # Write all rows at once

def string_to_list_of_dicts(s):
    s = s.strip()
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
    items = s.split('},')
    result = []
    
    for item in items:
        item = item.strip().strip('{}')
        if item:
            kv_pairs = item.split(',')
            d = {}
            for pair in kv_pairs:
                if ':' in pair:
                    key, value = pair.split(':', 1)
                    d[key.strip().strip('"')] = value.strip().strip('"')
            result.append(d)
    
    return result

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

def user_placement(username):
    row = read_info()
    placement = -1
    for item in row:
        placement += 1
        print(item[0])
        print(username)
        if item[0] == username:
            print("found!")
            return placement
