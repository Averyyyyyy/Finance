# Samuel Andelin, Personal Finances

from utils import read_info, save_info, string_to_list_of_dicts, list_of_dicts_to_string

# sign in function
def sign_in():
    while True:
        # user input to sign in, sign up, be anonymous, or exit
        choice = input("Type 1 to sign in, type 2 to sign up, and type 3 to exit.\n-->")

        # if the user wants to sign in
        if choice == "1":
            while True:
                # variable whether to exit or not
                go_to_first_choice = False

                # username login loop
                while True:
                    # variable whether to loop back or not
                    loopback = True

                    # user input for username
                    username = input("What is your username?(or type exit to exit)\n-->").strip()

                    # if user wants to exit
                    if username.lower() == "exit":
                        go_to_first_choice = True
                        break

                    # reads all usernames and compares them to user input
                    users = read_info()
                    for user in users:
                        if username == user['username']:
                            loopback = False
                            break

                    # if the username isn't found        
                    if loopback:
                        print("Username not found!!!")
                        continue
                    else:
                        break

                if go_to_first_choice:
                    break

                # loop for password checking
                while True:
                    # variable to loopback or not
                    loopback = True

                    # user input for password
                    password = input("What is your password?(or type exit to exit)\n-->").strip()

                    # if the user wants to exit
                    if password.lower() == "exit":
                        go_to_first_choice = True
                        break

                    # reads all passwords and compares them
                    users = read_info()
                    for user in users:
                        if username == user['username']:
                            # if user input matches
                            if password == user['password']:
                                print("Signed in successfully!")
                                return username
                            # if user input doesn't match
                            else:
                                print("Invalid password!")
                                break

                    if loopback:
                        continue

                if go_to_first_choice:
                    break

        # if the user wants to make an account        
        elif choice == "2":
            while True:
                # variable for looping back or not
                loopback = False

                # user input to create a new account username
                username = input("What is the username that you want to create?\n-->").strip()

                # if the user wants to make their username "exit" tell them no
                if username.lower() == "exit":
                    print("Don't use that username please.")
                    continue

                # checks if the username is already taken
                users = read_info()
                for user in users:
                    if username == user['username']:
                        print("Username is already taken!")
                        loopback = True

                # if the program needs to loop back, do so
                if loopback:
                    continue

                # if not, exit the create username section
                else:
                    break

            while True:
                # user input to create a new account password
                password = input("What is the password that you want to create?\n-->").strip()

                # if the user wants to make their password "exit" tell them no
                if password.lower() == "exit":
                    print("Don't use that password please.")
                    continue

                # verification of password
                confirm_password = input("Please type your password again to confirm.\n-->")

                # if passwords match, input all info
                if password == confirm_password:
                    print("Username of", username, "and password of", password, "has been inputted successfully!")
                    users.append({
                        "username": username,
                        "incomes": [],
                        "expenses": [],
                        "goals": [],
                        "current_worth": 0,
                        "password": password
                    })
                    save_info(users)
                    break

                # if passwords don't match, loop back
                else:
                    print("Passwords do not match!!!")
                    continue

        # if the user wants to exit
        elif choice == "3":
            return "exit"

        # if the user is stupid and can't figure out how to type a good input
        else:
            print("Not a valid option!")