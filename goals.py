#Alex Anderson, Savings Goal Tracker

import csv
from utils import read_info, save_info, string_to_list_of_dicts, list_of_dicts_to_string
import csv
import ast
import matplotlib.pyplot as plt

def goals_tracker(placement,username):
    row = read_info()
    current_goals = []

    try:
        current_goals = string_to_list_of_dicts(row[placement]["goals"])
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

    row[placement]["goals"] = list_of_dicts_to_string(current_goals)
    save_info(row)
    bar_graph(username)
    return current_goals





#-------------------End of Alex's Code----------------------



#-------------------Start of Samuel's Code---------------------

import csv
import ast
import matplotlib.pyplot as plt

def bar_graph(username):
    with open("info.csv", "r") as file:
        csv_reader = csv.reader(file)
        found_data = False  # Flag to track if we find the username and data
        
        for line in csv_reader:
            if len(line) > 1:  # Ensure there's more than one column
                csv_username = line[0].strip()
                
                if csv_username.lower() == username.lower():
                    found_data = True

                    try:
                        goals_data = line[3].strip()  # Retrieve the goals column
                        goals = ast.literal_eval(goals_data)  # Safely evaluate the cleaned data

                        # Prepare data for the bar graph
                        goal_titles = [goal["goal_name"] for goal in goals]
                        targets = [goal["goal_amount"] for goal in goals]
                        current = [goal["earned"] for goal in goals]

                        # Bar setup
                        x = range(len(goal_titles))  # x locations for the groups
                        bar_width = 0.4  # Set bar width

                        plt.figure(figsize=(10, 6))  # Set the figure size

                        # Create target bars
                        plt.bar(x, targets, width=bar_width, label='Target', color='lightblue', align='center')
                        # Create current bars in front of target bars
                        plt.bar(x, current, width=bar_width, label='Current', color='orange', align='center')

                        # Adding data labels on top of current bars
                        for i in range(len(goal_titles)):
                            plt.text(i, current[i] + 50, str(current[i]), ha='center', va='bottom')

                        # Labeling the bars
                        plt.xlabel('Goals')
                        plt.ylabel('Values')
                        plt.title(f'Goals vs. Current Progress for {username}')
                        plt.xticks(x, goal_titles)  # Center the goal titles
                        plt.legend()
                        plt.ylim(0, max(targets) * 1.1)  # Set y-axis limit with a margin
                        plt.tight_layout()  # Adjust layout to make sure everything fits without overlap
                        plt.show()

                    except Exception as e:
                        print(f"Error processing goals for {username}: {e}")

        if not found_data:
            print(f"No data found for username: {username}")
