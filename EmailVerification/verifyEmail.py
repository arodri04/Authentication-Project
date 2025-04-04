import random
from createEmail import *

users = {"hnkblarg@gmail.com": ["123", "This is the Secret Message"],
        "": ["1234", "This is the Secret Message number 2"]}

def verify(usern, pwd):
    if usern in users and users[usern][0] == pwd:
        verifNumber = random.randint(0,999999)
        vnum = f"{verifNumber:06d}"
        sendEmail(usern, vnum)
        inputNumber = input("Secondary Identification Required, Please check email and enter 6 digit number: ")
        if inputNumber == vnum:
            print(users[usern][1])
        else: 
            print("could not verify")
    else:
        print("could not verify")



uname = input("Please enter Email: ")
passwd = input("Please enter password: ")
verify(uname, passwd)
