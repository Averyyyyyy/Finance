#Alex Anderson, Budgeting

import csv
from utils import read_info, save_info, string_to_list_of_dicts, list_of_dicts_to_string

def set_budget(placement):
    row = read_info()
    try:
        expense_list = string_to_list_of_dicts(row[placement][2])
    except IndexError:
        print("Error: Malformed expense data.")
        expense_list = []

    category = input("Enter the category you want to set a budget for: ")
    while True:
        try:
            budget_limit = float(input("Enter the budget limit: "))
            break
        except ValueError:
            print("That is not a valid number.")
            continue

    for expense in expense_list:
        if expense.get("category") == category:
            expense["budget_limit"] = budget_limit
            print("Budget limit for", category, "set to", budget_limit)

    row[placement][2] = list_of_dicts_to_string(expense_list)
    save_info(row)
    return expense_list