#Alex Anderson, Income Tracking

from storing import load_user_data
from datetime import datetime
import csv
import numpy as np
import matplotlib.pyplot as plt

# Function incomes_maker
def incomes_maker():

#     incomes equals an empty list
    incomes = []

#     Display "What is the number of income sources you have?"
#     income_sources equals Input
    while True:
        try:
            income_sources = int(input("What is the number of income sources you have?: "))
            break
        except:
            print("That is not a number")
            continue

#     For the number from 1 to income_sources do:
    for number in range(income_sources):
#         Display "Enter income source name:"
#         income_source equals Input
        income_source = input("Enter income source name:")
        
#         Display "Enter the amount this income earns:"
#         income_amount equals Input
        while True:
            try:
                income_amount = float(input("Enter the amount this income earns: "))
                break
            except:
                print("That is not a number")
                continue
        
#         Display "How often do you earn this amount? (Enter days, 0 if one-time):"
#         income_timeframe equals Input
        while True:
            try:
                income_timeframe = int(input("How often do you earn this amount? (Enter days, 0 if it is a one time thing): "))
                break
            except:
                print("That is not a number")
                continue
        
#         income equals {
        income = {
#             "source": income_source,
            "source": income_source,

#             "amount": income_amount,
            "amount": income_amount,

#             "time": income_timeframe
            "time": income_timeframe

#         }
        }
        
#         Append income to incomes
        incomes.append(income)

#     End For
# Run Averys Function
    load_user_data(incomes)

# End the function
    return incomes


#--------------Alex's code ends----------------------


#--------------Samuel's Code starts-----------------------
def line_graph():
    with open("info.csv", "r") as file:
        incomes = []
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            for income in line[1]:
                incomes.append(line[1])

        dates = []
        for income in incomes:
            dates.append(income["date"])
        amounts = []
        for income in incomes:
            amounts.append(income["amount"])
        
        print(incomes)
        print(amounts)


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

line_graph()