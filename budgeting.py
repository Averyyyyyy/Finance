#Alex Anderson, Budgeting

from info import *

# function to set up or update a budget limit for a category
def set_budget():
    row = safe_read_info()
    try:
        expense_list = string_to_list_of_dicts(row[2])
    except:
        print("Error: Malformed expense data.")
        expense_list = []

    category = input("Enter the category you want to set a budget for: ")
    while True:
        try:
            budget_limit = float(input("Enter the budget limit: "))
            break
        except:
            print("That is not a valid number.")
            continue

    # set the budget for the category
    for expense in expense_list:
        if expense["category"] == category:
            expense["budget_limit"] = budget_limit
            print("Budget limit for", category, "set to", budget_limit)

    row[2] = list_of_dicts_to_string(expense_list)
    save_info(row)
    return expense_list