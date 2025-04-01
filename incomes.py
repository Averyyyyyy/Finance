#Alex Anderson, Income Tracking

from storing import saving

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
    saving(incomes)

# End the function
    return incomes