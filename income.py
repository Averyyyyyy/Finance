#Alex Anderson, Income Tracking

from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
import ast
from utils import read_info, save_info, string_to_list_of_dicts, list_of_dicts_to_string

def income_entry(placement):
    row = read_info()
    try:
        income_list = string_to_list_of_dicts(row[placement]["incomes"])
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

    for _ in range(count):

        while True:
            date = input("Enter the date (YYYY-MM-DD): ")
            dash_amount = date.count("-")
            
            def count_integers(input_string):
                parts = input_string.split('-')
                count = 0
                for part in parts:
                    if part.strip().isdigit():
                        count += 1
                return count
            
            number_amount = count_integers(date)

            if dash_amount != 2 or number_amount != 3:
                print("that is not a correct date.")
                continue

            else: 
                break

        source = input("Enter the income source: ")
        while True:
            try:
                amount = float(input("Enter the income amount: "))
                break

            except ValueError:
                print("That is not a valid number.")
                continue

        income = {
            "date": date,
            "source": source,
            "amount": amount
        }

        income_list.append(income)

    row[placement]["incomes"] = list_of_dicts_to_string(income_list)
    save_info(row)


#--------------Alex's code ends----------------------


#--------------Samuel's Code starts-----------------------
import csv
import ast
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def line_graph(username):
    with open("info.csv", "r") as file:
        csv_reader = csv.reader(file)
        found_data = False  # Flag to track if we find the username and data
        
        for line in csv_reader:
            if len(line) > 1:  # Ensure there's more than one column
                csv_username = line[0].strip()
                
                if csv_username.lower() == username.lower():
                    found_data = True

                    try:
                        cleaned_data = line[1].strip()  # Remove extra spaces
                        data = ast.literal_eval(cleaned_data)  # Safely evaluate the cleaned data

                        # Extract valid incomes with correct formats
                        incomes = []
                        for entry in data:
                            if isinstance(entry, dict) and "date" in entry and "amount" in entry:
                                try:
                                    # Validate date format
                                    date_obj = datetime.strptime(entry["date"], "%Y-%m-%d")
                                    incomes.append(entry)
                                except ValueError:
                                    continue  # Skip invalid dates

                        filtered_incomes = [(income["date"], float(income["amount"])) for income in incomes]

                        if not filtered_incomes:
                            print("Error: No valid data to process.")
                            return

                        # Split filtered data back into dates and amounts
                        filtered_dates, filtered_amounts = zip(*filtered_incomes)

                        # Convert string dates to datetime objects
                        date_objects = [datetime.strptime(date, "%Y-%m-%d") for date in filtered_dates]

                        # Fit a linear regression line to the data
                        date_numbers = mdates.date2num(date_objects)
                        coefficients = np.polyfit(date_numbers, filtered_amounts, 1)
                        slope, intercept = coefficients
                        money_fit = slope * date_numbers + intercept

                        # Create a figure with a larger size
                        plt.figure(figsize=(12, 6))  # Width, Height in inches

                        # Plot the original data and the fitted line
                        plt.scatter(date_objects, filtered_amounts, color='blue', label='Data points')
                        step = max(1, len(date_objects) // 10)  # Only plot up to 10 points
                        plt.plot(date_objects[::step], money_fit[::step], color='red', label='Fitted line')

                        # Formatting the plot
                        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Format to year-month
                        tick_pos = date_objects[:: (len(date_objects) // 5 + 1)]  # Adjust this to control frequency
                        plt.xticks(tick_pos, rotation=45, ha='right')

                        plt.xlabel('Date')
                        plt.ylabel('Money Amount ($)')
                        plt.title(f'Money Amount Trend for {username} Over Time')
                        plt.legend()
                        plt.tight_layout()
                        plt.show()

                    except Exception as e:
                        print(f"Error processing line for {username}: {e}")

        if not found_data:
            print(f"No data found for username: {username}")

