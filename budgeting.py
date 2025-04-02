#Alex Anderson, Budgeting

# Function budgeting
def budgeting(expenses):
    categorys = {}
    for expense in expenses:
        categorys.add(expense["category"])
#     Display "What category do you want to set a budget for?"
#     category equals Input
    print("What category do you want to set a budget for?")
    for category in categorys:
        print(category + ", ")
    
    category = input()
    
#     Display "What amount of money do you want to cap off at?"
#     cap equals Input
    
#     For each expense in expenses, do:
#         If expense["source"] is equal to category, then
#             expense["cap"] equals cap
            
#             If expense["amount"] is greater than cap, then
#                 Display "Warning: Your expense exceeds the cap!"
#             End If
#         End If
#     End For
    
#     Return category, cap to averys save function
# End the function
