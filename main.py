#Samuel Andelin, Personal Finances

#importing needed functions
from sign_in import * 
from income import income_entry
from expense import expense_entry
from budget import set_budget
from goals import goals_tracker
from conversion import convert_currency
from utils import user_placement

#main function
def main():
    print("Welcome to the personal finanace calculator!")

    #gets the username/signs in
    username = sign_in()

    #if the user wants to exit from the sign in function, do so
    if username == "exit":
        print("Ok, bye!")

    #function for going to manage finances
    def finances():
        while True:
            financechoice = input("Where do you want to go? (1 for income, 2 for expenses, 3 for budgeting, 4 for goals, 5 for conversions, and 6 to go back to the main frame)\n--> ")

            placement = user_placement(username)

            if financechoice == "1":
                income_entry(placement)
            elif financechoice == "2":
                expense_entry(placement)
            elif financechoice == "3":
                set_budget(placement)
            elif financechoice == "4":
                goals_tracker(placement)
            elif financechoice == "5":
                convert_currency()
            elif financechoice == "6":
                break
            else:
                print("Invalid input!")
    
    #visualizing function
    def visualize():
        while True:
            #choice to go to sections of financing
            visualizechoice = input("Where do you want to go? (1 for pie chart of expenses, 2 for line graph of incomes, 3 for bar graph of goals, and 4 to go back to the main frame)\n-->")

            #if the user wants to go to the pie chart function
            if visualizechoice == "1":
                pie_chart()
            #if the user wants to go to the line graph function
            elif visualizechoice == "2":
                line_graph()
            #if the user wants to go to the bar graph function
            elif visualizechoice == "3":
                bar_graph()
            #if the user wants to exit
            elif visualizechoice == "4":
                break
            #if the user's input is invalid
            else:
                print("Invalid input!")

    #main loop
    while True:
        #main frame choice
        choice = input("Where do you want to go?(1 for finances, 2 for visualize data, 3 to exit)\n-->")

        #if the user wants to manage finances
        if choice == "1":
            #goes to the finances function
            finances()
        elif choice == "2":
            #goes to visulizations
            visualize()

#Runs main
main()