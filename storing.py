#Avery bowman, finance project (my function name is saving)

import csv
import os
import json
import ast

def saving(data, data_type, index, csv_file='finance_data.csv'):
    """
    Save financial data to a CSV file in the specified format.
    
    Parameters:
    - data: The data to save
    - data_type: Type of data ('username', 'incomes', 'expenses', 'goals', 'current_worth', 'password')
    - index: Position in the CSV row where this data belongs (0-based)
    - csv_file: Path to the CSV file
    
    Returns:
    - True if successful, False otherwise
    """
    try:
        # Check if file exists and create if not
        file_exists = os.path.isfile(csv_file)
        
        # Load existing data
        rows = []
        if file_exists:
            with open(csv_file, 'r', newline='') as file:
                reader = csv.reader(file)
                rows = list(reader)
        
        # If file is empty or doesn't exist, create header row
        if not file_exists or len(rows) == 0:
            headers = ["username", "incomes", "expenses", "goals", "current_worth", "password"]
            rows = [headers]
        
        # Find user's row if username is provided and this is a username field
        user_row = None
        if data_type == 'username' and index == 0:
            for i, row in enumerate(rows):
                if i > 0 and row[0] == data:  # Skip header row
                    user_row = row
                    break
            
            # If username not found, create new row
            if user_row is None:
                user_row = [''] * 6  # Create a row with 6 empty fields
                user_row[0] = data   # Set username
                rows.append(user_row)
        
        # If we're updating something other than username
        else:
            # Find the user's row first (assuming username is in data[0])
            username = None
            for i, row in enumerate(rows):
                if i > 0 and row[0] == data[0]:  # Skip header, check username
                    user_row = row
                    break
            
            # Format the data properly based on type
            if data_type in ['incomes', 'expenses', 'goals']:
                # These fields expect a list of dictionaries as a string
                formatted_data = json.dumps(data[1])
            else:
                formatted_data = data[1]
            
            # Update the field if user found
            if user_row is not None:
                # Extend row if needed
                if index >= len(user_row):
                    user_row.extend([''] * (index - len(user_row) + 1))
                user_row[index] = formatted_data
        
        # Write all data back to the CSV file
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        
        print(f"Successfully saved {data_type} data to {csv_file}")
        return True
        
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

def load_data(username, csv_file='finance_data.csv'):
    """
    Load a user's financial data from the CSV file
    
    Parameters:
    - username: The username to look for
    - csv_file: Path to the CSV file
    
    Returns:
    - Dictionary with user data or None if not found
    """
    try:
        if not os.path.isfile(csv_file):
            return None
            
        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            
            # Find the user's row
            for i, row in enumerate(rows):
                if i > 0 and row[0] == username:  # Skip header
                    # Parse the data into appropriate types
                    user_data = {
                        'username': row[0],
                        'incomes': ast.literal_eval(row[1]) if row[1] else [],
                        'expenses': ast.literal_eval(row[2]) if row[2] else [],
                        'goals': ast.literal_eval(row[3]) if row[3] else [],
                        'current_worth': float(row[4]) if row[4] else 0,
                        'password': row[5] if len(row) > 5 else ''
                    }
                    return user_data
        
        return None
    
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Example usage:
# To create a new user:
# saving('example', 'username', 0)

# To update income:
# incomes = [{'date': '1111-11-11', 'source': 'a', 'amount': 1.0}]
# saving(['example', incomes], 'incomes', 1)

# To update expenses:
# expenses = [{'date': '1111-11-11', 'category': 'a', 'amount': 1.0, 'budget_limit': 1.0}]
# saving(['example', expenses], 'expenses', 2)

# To update goals:
# goals = [{'goal_name': 'a', 'goal_amount': 1.0, 'earned': 1.0}]
# saving(['example', goals], 'goals', 3)

# To update current worth:
# saving(['example', 0], 'current_worth', 4)

# To update password:
# saving(['example', 'password123'], 'password', 5)

# Take data from theres and find what the type of data is and save it to the appopeate place
# Use the word "saving" as the key word to know they are pulling form my code

# Load the new data to the csv file in the correct order

# Take what the index number they give me so I know where that item goes
    # So expenses is 1 so then the espenses will be the second item in the line on the csv

# A function that can run to whatever they call my function for, so if its like calling it to save the data then I will save it to a csv

# 1. Run the code if someone calls my function
# 2. Find out what type of data it is and save it in the correct order to the csv
# 3. Save the data to the csv