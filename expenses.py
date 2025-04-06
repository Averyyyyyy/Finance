#Alex Anderson, Expenses Tracking

from info import *

# function to add expense entries (date, amount, category)
def expense_entry():
    row = safe_read_info()
    try:
        expense_list = string_to_list_of_dicts(row[2])
    except:
        print("Error: Malformed expense data.")
        expense_list = []

    while True:
        try:
            count = int(input("How many expense entries do you want to add?: "))
            break
        except:
            print("That is not a valid number.")
            continue

    for i in range(count):
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the expense category: ")
        while True:
            try:
                amount = float(input("Enter the expense amount: "))
                break
            except:
                print("That is not a valid number.")
                continue

        # create expense dictionary and add it to the list
        expense = {
            "date": date,
            "category": category,
            "amount": amount
        }

        expense_list.append(expense)

    row[2] = list_of_dicts_to_string(expense_list)
    save_info(row)
    return expense_list


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
