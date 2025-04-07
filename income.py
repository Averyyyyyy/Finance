#Alex Anderson, Income Tracking

from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import csv
from utils import read_info, save_info, string_to_list_of_dicts, list_of_dicts_to_string

def income_entry(placement):
    row = read_info()
    try:
        income_list = string_to_list_of_dicts(row[placement][1])
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

    row[placement][1] = list_of_dicts_to_string(income_list)
    save_info(row)


#--------------Alex's code ends----------------------


#--------------Samuel's Code starts-----------------------
def line_graph():
    with open("info.csv", "r") as file:
        incomes = []
        csv_reader = csv.reader(file)
        for line in csv_reader:
            for income in line[1]:
                incomes.append(line[1])

        dates = []
        for income in incomes:
            dates.append(income["date"])
        amounts = []
        for income in incomes:
            amounts.append(income["amount"])


        #Convert each string date to a datetime object for proper comparison
        dates = [datetime.strptime(date, "%m/%d") for date in dates]

        #Sort the dates
        sorted_dates = sorted(dates)

        #Optionally convert back to string format
        sorted_dates_str = [date.strftime("%m/%d") for date in sorted_dates]

        # Example data points (x, y)
        x = np.array(sorted_dates_str)
        y = np.array(amounts)

        # Fit a line to the data points (1st degree polynomial = line)
        coefficients = np.polyfit(x, y, 1)

        # Create the fitted line using the coefficients
        fit_line = np.polyval(coefficients, x)

        # Plot the data points
        plt.scatter(x, y, color='red', label='Data points')

        # Plot the fitted line
        plt.plot(x, fit_line, label=f'Fitted line: y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}', color='blue')

        # Add labels and legend
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Predicted trend of incomes')
        plt.legend()

        # Show the plot
        plt.show()