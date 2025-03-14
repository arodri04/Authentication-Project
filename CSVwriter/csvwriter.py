import csv
import os
from datetime import datetime

header = [["id", "FirstName", "LastName"]]
doorHeader = [["id", "FirstName","LastName", "Time"]]
users = [[1, "Sam", "Rodriguez",], [2, "Tae", "Bailon"]]

def read_row(userID):
    with open("users.csv", "r") as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            if int(row[0]) == userID:
                doorTime(row)

def doorTime(user):
    with open("door1.csv", "a", newline="") as doorcsv:
        user.append(datetime.now().strftime("%m-%d-%Y %H:%M:%S"))
        csvwriter = csv.writer(doorcsv)        
        csvwriter.writerow(user)

read_row(2)