#Alex Anderson, Savings Goal Tracker

import csv
from utils import read_info, save_info, string_to_list_of_dicts, list_of_dicts_to_string

def goals_tracker(placement):
    row = read_info()
    current_goals = []

    try:
        current_goals = string_to_list_of_dicts(row[placement][3])
    except IndexError:
        print("No existing goals found.")
    
    if current_goals:
        choice = input("Do you want to 1(make new goals) or 2(add to previous goals): ")
        if choice == "1":
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

    row[placement][3] = list_of_dicts_to_string(current_goals)
    save_info(row)
    return current_goals