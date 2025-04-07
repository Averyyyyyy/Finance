#Alex Anderson, Currency Conversion Feature

def convert_currency():
    amount = float(input("Enter the amount to convert: "))
    currency = input("Enter the currency to convert to (yen, euros, pounds): ")

    if currency == "yen":
        print(f"Amount in yen: {amount * 148.41}")
    elif currency == "euros":
        print(f"Amount in euros: {amount * 0.92}")
    elif currency == "pounds":
        print(f"Amount in pounds: {amount * 0.77}")
    else:
        print("Invalid currency choice.")
