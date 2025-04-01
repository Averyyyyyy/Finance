#Alex Anderson, Expenses Tracking

# Function expenses_maker
#     expenses equals an empty list
#     Display "What is the number of expense sources you have?"
#     expense_sources equals Input

#     For the number from 1 to expense_sources do:
#         Display "Enter expense source name:"
#         expense_source equals Input
        
#         Display "Enter the amount you lose:"
#         expense_amount equals Input
        
#         Display "How often do you lose this amount? (Enter in days, 0 if one-time):"
#         expense_timeframe equals Input
        
#         expense equals {
#             "source": expense_source,
#             "amount": expense_amount,
#             "time": expense_timeframe,
#             "cap": NULL
#         }
        
#         Append expense to expenses
#     End For

#     Return expenses to averys save function
# End the function