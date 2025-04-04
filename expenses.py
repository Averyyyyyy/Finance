#Alex Anderson, Expenses Tracking

import csv
import ast
from info import read_info, save_info

# Add expense entries (date, amount, category)
def expense_entry():
    row = read_info()
    expense_list = ast.literal_eval(row[2])  # convert string to list

    while True:
        try:
            count = int(input("How many expense entries do you want to add?: "))
            break
        except:
            print("That is not a number")
            continue

    for i in range(count):
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the expense category: ")
        while True:
            try:
                amount = float(input("Enter the expense amount: "))
                break
            except:
                print("That is not a number")
                continue

        # create expense dictionary and add it to the list
        expense = {
            "date": date,
            "category": category,
            "amount": amount
        }

        expense_list.append(expense)

    row[2] = str(expense_list)
    save_info(row)
    return expense_list
