#Alex Anderson, Budgeting

import csv
import ast
from expenses import expense_entry  # Import expense-related function
from info import read_info, save_info

# Set or update a budget limit for a category
def set_budget():
    row = read_info()
    expense_list = ast.literal_eval(row[2])  # Convert string to list

    category = input("Enter the category you want to set a budget for: ")
    while True:
        try:
            budget_limit = float(input("Enter the budget limit: "))
            break
        except:
            print("That is not a number")
            continue

    for expense in expense_list:
        if expense["category"] == category:
            expense["budget_limit"] = budget_limit
            print(f"Budget limit for {category} set to {budget_limit}")

    row[2] = str(expense_list)
    save_info(row)
    return expense_list