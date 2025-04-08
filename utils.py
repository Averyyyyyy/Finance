#Alex Anderson, file that converts,saves, and loads info from csv

import csv
import ast  # For safely evaluating string representations of Python objects

# Read information from CSV file
def read_info():
    try:
        with open("info.csv", "r") as file:
            reader = csv.DictReader(file)
            rows = []
            for row in reader:
                # Strip spaces from keys to avoid issues with extra spaces in column names
                row = {key.strip(): value for key, value in row.items()}  # Strip extra spaces from column names
                # Convert string representations of lists/dicts to actual lists/dicts
                row['incomes'] = ast.literal_eval(row['incomes'])
                row['expenses'] = ast.literal_eval(row['expenses'])
                row['goals'] = ast.literal_eval(row['goals'])
                row['current_worth'] = int(row['current_worth'])
                rows.append(row)
            return rows
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return []

# Save information to CSV file
def save_info(data):
    try:
        with open("info.csv", "w", newline="") as file:
            fieldnames = data[0].keys()  # Get the fieldnames from the first row's keys
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Write the header (column names)
            for row in data:
                # Convert lists/dicts back to their string representations before saving
                row['incomes'] = row['incomes']
                row['expenses'] = row['expenses']
                row['goals'] = row['goals']
                row['current_worth'] = str(row['current_worth'])  # Ensure it's saved as a string
            writer.writerows(data)  # Write all rows at once
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

# Convert string to list of dictionaries (for goals, incomes, etc.)
def string_to_list_of_dicts(s):
    try:
        # Safe parsing of the string using ast.literal_eval
        return ast.literal_eval(s)
    except (ValueError, SyntaxError) as e:
        print(f"Error parsing string to list of dicts: {e} for string: {s}")
        return []  # Return an empty list if parsing fails

# Convert list of dictionaries back to a string representation
def list_of_dicts_to_string(lst):
    try:
        return str(lst)  # Convert the list of dicts back to a string
    except Exception as e:
        print(f"Error converting list of dicts to string: {e}")
        return "[]"

# Find the placement of a user (return the index in the CSV file)
def user_placement(username):
    rows = read_info()  # Read all rows
    for placement, item in enumerate(rows):
        # Ensure the row has the 'username' column and compare the username
        if item['username'].strip() == username:
            return placement
    return None  # Return None if username is not found

# Function to handle income entry
def income_entry(placement):
    # Ensure that placement is valid and exists
    if placement is None:
        print("Error: User not found!")
        return

    rows = read_info()
    if placement >= len(rows):
        print("Error: Invalid placement!")
        return
    
    # Access the 'incomes' key correctly and convert it
    income_list = string_to_list_of_dicts(rows[placement]['incomes'])  
    print(f"Income list for user {rows[placement]['username']}: {income_list}")
    # Further processing of income...