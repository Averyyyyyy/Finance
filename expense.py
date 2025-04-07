#Alex Anderson, Expenses Tracking

import csv
from utils import read_info, save_info, string_to_list_of_dicts, list_of_dicts_to_string

def expense_entry():
    row = read_info()
    try:
        expense_list = string_to_list_of_dicts(row[2])
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

    row[2] = list_of_dicts_to_string(expense_list)
    save_info(row)
    return expense_list