# Alex Anderson all code

import csv

# info file---------------------------------------------------------------------------
# Function that reads all data and returns it as a list of lists
def read_info():
    with open("info.csv", "r") as file:
        reader = csv.reader(file)
        return [row for row in reader]  # Return all rows as a list of lists

# Function that writes the updated data back into info.csv
def save_info(data):
    with open("info.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)  # Write all rows at once

# Function to safely read the csv file and return data
def safe_read_info():
    try:
        return read_info()
    except Exception as e:
        print("Error reading info.csv:", e)
        return []

# Function to convert a string to a list of dictionaries
def string_to_list_of_dicts(s):
    s = s.strip()
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
    items = s.split('},')
    result = []
    
    for item in items:
        item = item.strip().strip('{}')
        if item:
            kv_pairs = item.split(',')
            d = {}
            for pair in kv_pairs:
                if ':' in pair:
                    key, value = pair.split(':', 1)
                    d[key.strip().strip('"')] = value.strip().strip('"')
            result.append(d)
    
    return result

# Function to convert a list of dictionaries to a string
def list_of_dicts_to_string(lst):
    result = "["
    for d in lst:
        result += "{"
        for key, value in d.items():
            result += f'"{key}": "{value}", '
        result = result.rstrip(', ')
        result += "}, "
    result = result.rstrip(', ')
    result += "]"
    return result

# incomes file---------------------------------------------------------------------
# Function to do incomes
def income_entry():
    row = safe_read_info()
    try:
        income_list = string_to_list_of_dicts(row[1])
    except IndexError:
        print("Malformed income data.")
        income_list = []

    while True:
        try:
            count = int(input("How many income entries do you want to add?: "))
            break
        except ValueError:
            print("That is not a valid number.")
            continue

    for i in range(count):
        date = input("Enter the date (YYYY-MM-DD): ")
        source = input("Enter the income source: ")
        while True:
            try:
                amount = float(input("Enter the income amount: "))
                break
            except ValueError:
                print("That is not a valid number.")
                continue

        # Create income dictionary and add it to the list
        income = {
            "date": date,
            "source": source,
            "amount": amount
        }

        income_list.append(income)

    row[1] = list_of_dicts_to_string(income_list)
    save_info(row)
    return income_list

# budget file--------------------------------------------------------------------------
# Function to set up or update a budget limit for a category
def set_budget():
    row = safe_read_info()
    try:
        expense_list = string_to_list_of_dicts(row[2])
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

    # Set the budget for the category
    for expense in expense_list:
        if expense.get("category") == category:  # Use .get() for safety
            expense["budget_limit"] = budget_limit
            print("Budget limit for", category, "set to", budget_limit)

    row[2] = list_of_dicts_to_string(expense_list)
    save_info(row)
    return expense_list

# conversion file--------------------------------------------------------------------------
# Function to convert currencies
def convert_currency():
    while True:
        try:
            amount = float(input("Enter the amount to convert in dollars: "))
            break
        except ValueError:
            print("That is not a valid number.")
            continue

    currency = input("Enter the currency to convert to (yen, euros, or pounds): ")

    if currency == "yen":
        print("Amount in yen:", amount * 148.41)
    elif currency == "euros":
        print("Amount in euros:", amount * 0.92)
    elif currency == "pounds":
        print("Amount in pounds:", amount * 0.77)
    else:
        print("Invalid currency choice.")

# expenses file----------------------------------------------------------------------------
# Function to add expense entries (date, amount, category)
def expense_entry():
    row = safe_read_info()
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

    for i in range(count):
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the expense category: ")
        while True:
            try:
                amount = float(input("Enter the expense amount: "))
                break
            except ValueError:
                print("That is not a valid number.")
                continue

        # Create expense dictionary and add it to the list
        expense = {
            "date": date,
            "category": category,
            "amount": amount
        }

        expense_list.append(expense)

    row[2] = list_of_dicts_to_string(expense_list)
    save_info(row)
    return expense_list

# goal file-----------------------------------------------------------------------------------
# Function that sets new goals or adds to previous goals
def goals_tracker():
    row = safe_read_info()
    current_goals = []

    # If there are existing goals, load them
    try:
        current_goals = string_to_list_of_dicts(row[3])
    except IndexError:
        print("No existing goals found.")
    
    if current_goals:
        choice = input("Do you want to 1(make new goals) or 2(add to previous goals): ")
        if choice == "1":
            # Make a new goal
            goal_name = input("Enter the goal name: ")
            while True:
                try:
                    goal_amount = float(input("Enter the goal amount: "))
                    break
                except ValueError:
                    print("That is not a valid number.")
                    continue
            while True:
                try:
                    earned = float(input("Enter the amount earned towards the goal: "))
                    break
                except ValueError:
                    print("That is not a valid number.")
                    continue
            current_goals.append({
                'goal_name': goal_name,
                'goal_amount': goal_amount,
                'earned': earned
            })
            print("New goal", goal_name, "added with a target of", goal_amount, "and earned", earned)

        elif choice == "2":
            # Add to an existing goal
            print("Existing goals:")
            for i in range(len(current_goals)):
                print(i + 1, ".", current_goals[i]['goal_name'], "- Target:", current_goals[i]['goal_amount'], "- Earned:", current_goals[i]['earned'])

            goal_choice = int(input("Enter the number of the goal you want to add to: ")) - 1

            if 0 <= goal_choice < len(current_goals):
                while True:
                    try:
                        additional_earned = float(input("Enter the additional amount earned: "))
                        break
                    except ValueError:
                        print("That is not a valid number.")
                        continue
                current_goals[goal_choice]['earned'] += additional_earned
                print("Added", additional_earned, "to goal", current_goals[goal_choice]['goal_name'])
            else:
                print("Invalid goal number.")

    else:
        print("No existing goals, creating a new goal")
        goal_name = input("Enter the goal name: ")
        while True:
            try:
                goal_amount = float(input("Enter the goal amount: "))
                break
            except ValueError:
                print("That is not a valid number.")
                continue
        while True:
            try:
                earned = float(input("Enter the amount earned towards the goal: "))
                break
            except ValueError:
                print("That is not a valid number.")
                continue
        current_goals.append({
            'goal_name': goal_name,
            'goal_amount': goal_amount,
            'earned': earned
        })

    # Saves the updated goals back to the csv
    row = safe_read_info()
    row[3] = list_of_dicts_to_string(current_goals)
    save_info(row)
    return current_goals

# finances function to navigate through sections of financing
def finances():
    while True:
        # Choice to go to sections of financing
        financechoice = input("Where do you want to go? (1 for income, 2 for expenses, 3 for budgeting, 4 for goals, 5 for conversions, and 6 to go back to the main frame)\n--> ")

        # If the user wants to go to incomes
        if financechoice == "1":
            income_list = income_entry()
        # If the user wants to go to expenses
        elif financechoice == "2":
            expense_list = expense_entry()
        # If the user wants to go to budgeting
        elif financechoice == "3":
            budget_list = set_budget()
        # If the user wants to go to goals
        elif financechoice == "4":
            current_goals = goals_tracker()
        # If the user wants to go to conversions
        elif financechoice == "5":
            convert_currency()
        # If the user wants to exit
        elif financechoice == "6":
            break
        # If the user's input is invalid
        else:
            print("Invalid input!")