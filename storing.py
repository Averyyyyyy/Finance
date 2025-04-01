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

# take data from theres and find what the type of data is and save it to the appopeate place