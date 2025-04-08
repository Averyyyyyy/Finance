#Alex Anderson, file that converts,saves, and loads info from csv

import csv
import ast

# Read information from CSV file
def read_info():
    try:
        with open("info.csv", "r", newline='') as file:
            reader = csv.DictReader(file)
            rows = []
            for row in reader:
                # Strip spaces from keys to avoid issues with extra spaces in column names
                row = {key.strip(): value for key, value in row.items()}

                # Convert string representations of lists/dicts to actual lists/dicts
                row['incomes'] = string_to_list_of_dicts(row.get('incomes', '[]'))
                row['expenses'] = string_to_list_of_dicts(row.get('expenses', '[]'))
                row['goals'] = string_to_list_of_dicts(row.get('goals', '[]'))
                row['current_worth'] = int(row.get('current_worth', 0))
                rows.append(row)
            return rows
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return []

# Save information to CSV file
def save_info(data):
    try:
        with open("info.csv", "w", newline='') as file:
            fieldnames = ['username', 'incomes', 'expenses', 'goals', 'current_worth', 'password']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for row in data:
                # Convert back to string form before saving
                row['incomes'] = list_of_dicts_to_string(row.get('incomes', []))
                row['expenses'] = list_of_dicts_to_string(row.get('expenses', []))
                row['goals'] = list_of_dicts_to_string(row.get('goals', []))
                row['current_worth'] = str(row.get('current_worth', 0))
                writer.writerow(row)
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

# Convert string to list of dictionaries (for goals, incomes, etc.)
def string_to_list_of_dicts(s):
    try:
        if isinstance(s, list):
            return s  # Already a list
        return ast.literal_eval(s)
    except (ValueError, SyntaxError) as e:
        print(f"Error parsing string to list of dicts: {e} for string: {s}")
        return []

# Convert list of dictionaries back to a string representation
def list_of_dicts_to_string(lst):
    try:
        return str(lst)
    except Exception as e:
        print(f"Error converting list of dicts to string: {e}")
        return "[]"

# Find the placement of a user (return the index in the CSV file)
def user_placement(username):
    rows = read_info()
    for placement, item in enumerate(rows):
        if item['username'].strip() == username:
            return placement
    return None