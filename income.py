#Alex Anderson, Income Tracking

from storing import load_user_data
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
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
def line_graph(username):
    with open("info.csv", "r") as file:
        csv_reader = csv.reader(file)
        found_data = False  # Flag to track if we find the username and data
        for line in csv_reader:
            # Print the raw line to check the data structure
            print("Raw line:", line)  # See the entire line being read

            if len(line) > 1:  # Ensure there's more than one column
                # Print and check the raw username before stripping whitespace
                print(f"Raw username in CSV: '{line[0]}'")

                # Clean the username and print it to ensure correct stripping
                csv_username = line[0].strip()
                print(f"Stripped username from CSV: '{csv_username}'")

                # Compare usernames case-insensitively and after stripping whitespace
                if csv_username.lower() == username.lower():  # Case insensitive comparison
                    found_data = True
                    print(f"Found data for username: {username}")

                    # Process line[1] which is expected to be a list of dictionaries
                    try:
                        # Clean up the line[1] to make sure it's properly formatted
                        cleaned_data = f"[{line[1]}]"
                        print(f"Cleaned data for {username}:", cleaned_data)

                        # Try parsing the cleaned data into a list of lists
                        data = ast.literal_eval(cleaned_data)  # Safely evaluate the cleaned data
                        print(f"Parsed data for {username}:", data)  # Check parsed data

                        # Extract the incomes, only focusing on those that have a "date" and "amount"
                        incomes = []
                        for entry in data:
                            if isinstance(entry, dict) and "date" in entry and "amount" in entry:
                                incomes.append(entry)

                        # Extract dates and amounts
                        dates = [income["date"] for income in incomes]
                        amounts = [float(income["amount"]) for income in incomes]  # Convert amounts to float

                        # Debugging: Print out the extracted dates and amounts
                        print("Dates:", dates)
                        print("Amounts:", amounts)

                        # Ensure that the dates and amounts are not empty
                        if not dates or not amounts:
                            print("Error: No data to process.")
                            return

                        # Assume a common year (e.g., 2025) and convert to datetime objects
                        year = 2025
                        date_objects = [datetime.strptime(f"{year}-{date}", "%Y-%m-%d") for date in dates]

                        # Convert dates to numbers (days since the start of the year)
                        date_numbers = mdates.date2num(date_objects)

                        # Debugging: Print out the date numbers
                        print("Date numbers:", date_numbers)

                        # Fit a line (1st degree polynomial) to the data points (dates -> money amounts)
                        coefficients = np.polyfit(date_numbers, amounts, 1)  # 1 means a linear fit

                        # Get the slope (m) and intercept (b)
                        slope, intercept = coefficients

                        # Generate the fitted line
                        money_fit = slope * date_numbers + intercept

                        # Plot the original data points
                        plt.scatter(date_objects, amounts, color='blue', label='Data points')

                        # Plot the fitted line
                        plt.plot(date_objects, money_fit, color='red', label='Fitted line')

                        # Format the x-axis to show dates properly
                        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
                        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

                        # Rotate date labels for better readability
                        plt.xticks(rotation=45)

                        # Add labels and title
                        plt.xlabel('Date')
                        plt.ylabel('Money Amount ($)')
                        plt.title(f'Money Amount Trend for {username} Over Time')

                        # Show legend
                        plt.legend()

                        # Show the plot
                        plt.tight_layout()  # Ensure the layout fits well
                        plt.show()

                    except Exception as e:
                        print(f"Error parsing line[1] for {username}: {e}")

        if not found_data:
            print(f"No data found for username: {username}")

# Run the function with a test username
line_graph("Samuel")