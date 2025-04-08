#Alex Anderson, Currency Conversion Feature

def convert_currency():
    while True:
        try:
            amount = float(input("Enter the amount to convert in dollars: "))
            break
        except ValueError:
            print("That is not a valid number.")
            continue

    currency = input("Enter the currency to convert to (yen, euros, or pounds): ")

    if currency == "yen":
        print("Amount in yen:", amount * 148.41)
    elif currency == "euros":
        print("Amount in euros:", amount * 0.92)
    elif currency == "pounds":
        print("Amount in pounds:", amount * 0.77)
    else:
        print("Invalid currency choice.")
