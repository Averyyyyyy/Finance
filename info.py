#Alex Anderson, pulls info and adds info to csv file

import csv

# Reads the data from info.csv and returns it as a list
def read_info():
    with open("info.csv", "r") as file:
        reader = csv.reader(file)
        row = next(reader)
        return row

# Writes the updated data back into info.csv
def save_info(row):
    with open("info.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)