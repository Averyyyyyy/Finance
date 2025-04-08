#Alex Anderson, Expenses Tracking

import csv
from utils import read_info, save_info, string_to_list_of_dicts, list_of_dicts_to_string

def expense_entry(placement,username):
    row = read_info()
    try:
        expense_list = string_to_list_of_dicts(row[placement]["expenses"])
    except IndexError:
        print("Error: Malformed expense data.")
        expense_list = []

    while True:
        try:
            count = int(input("How many expense entries do you want to add?: "))
            break
        except ValueError:
            print("That is not a valid number.")
            continue

    for _ in range(count):
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the expense category: ")
        while True:
            try:
                amount = float(input("Enter the expense amount: "))
                break
            except ValueError:
                print("That is not a valid number.")
                continue

        expense = {
            "date": date,
            "category": category,
            "amount": amount
        }

        expense_list.append(expense)

    row[placement]["expenses"] = list_of_dicts_to_string(expense_list)
    save_info(row)
    pie_chart(username)



#----------End of Alex's Code------------




#----------Start of Samuel's Code--------------
import csv
import ast
import matplotlib.pyplot as plt

def pie_chart(username):
    with open("info.csv", "r") as file:
        csv_reader = csv.reader(file)
        found_data = False  # Flag to track if we find the username and data
        
        for line in csv_reader:
            if len(line) > 1:  # Ensure there's more than one column
                csv_username = line[0].strip()
                
                if csv_username.lower() == username.lower():
                    found_data = True

                    try:
                        expenses_data = line[2].strip()  # Extracting the expenses from the 3rd column
                        expenses = ast.literal_eval(expenses_data)  # Safely evaluate the cleaned data

                        # Prepare data for the pie chart
                        expense_labels = [expense["category"] for expense in expenses]
                        expense_values = [expense["amount"] for expense in expenses]

                        # Create a pie chart
                        plt.figure(figsize=(8, 8))  # Set the figure size
                        plt.pie(expense_values, labels=expense_labels, autopct='%1.1f%%', startangle=90)
                        plt.title(f'Expenses Breakdown for {username}')
                        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                        plt.show()

                    except Exception as e:
                        print(f"Error processing expenses for {username}: {e}")

        if not found_data:
            print(f"No data found for username: {username}")

