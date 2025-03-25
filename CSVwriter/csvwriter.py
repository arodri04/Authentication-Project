import csv
import os
from datetime import datetime

header = [["id", "FirstName", "LastName"]]
doorHeader = [["id", "FirstName","LastName", "Time"]]
users = [[1, "Sam", "Rodriguez",], [2, "Tae", "Bailon"]]

def read_user(userID):
    with open("users.csv", "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if int(row[0]) == userID:
                doorTime(row)

def doorTime(user):
    with open("door1.csv", "a", newline="") as doorcsv:
        user.append(datetime.now().strftime("%m-%d-%Y %H:%M:%S"))
        csvwriter = csv.writer(doorcsv)     
        csvwriter.writerow(user)

def add_user(userID):
    with open("users.csv", "a", newline="") as file:
        csvwriter = csv.writer(file)
        first = input("Please Enter First Name: ")
        last = input("Please Enter Last Name: ")
        new_user = [userID, first, last]
        csvwriter.writerow(new_user)


read_user(2)