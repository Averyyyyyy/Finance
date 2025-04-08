#Avery bowman, finance project (my function name is saving)

import csv

USER_FILE = "user_finances.csv"

# Function to load user data from CSV
#after the user has singed in (need to add this part still)
def load_user_data(username):
   user_data = {"goals": [], "expenses": [], "incomes": []}

   try:
       with open(USER_FILE, mode="r", newline="") as file:
           reader = csv.DictReader(file)
           for row in reader:
               if row["username"] == username:
                   user_data["goals"] = eval(row["goals"]) if row["goals"] else []
                   user_data["expenses"] = eval(row["expenses"]) if row["expenses"] else []
                   user_data["incomes"] = eval(row["incomes"]) if row["incomes"] else []
                   return user_data
   except FileNotFoundError:
       print("User file not found. Creating a new one on save.")

# Take data from theres and find what the type of data is and save it to the appopeate place
# Use the word "saving" as the key word to know they are pulling form my code

# Load the new data to the csv file in the correct order

# Take what the index number they give me so I know where that item goes
    # So expenses is 1 so then the espenses will be the second item in the line on the csv

# A function that can run to whatever they call my function for, so if its like calling it to save the data then I will save it to a csv

# 1. Run the code if someone calls my function
# 2. Find out what type of data it is and save it in the correct order to the csv
# 3. Save the data to the csv

#added