users = {"test": ["123", "This is the Secret Message"],
        "test1": ["1234", "This is the Secret Message number 2"]}

def verify(usern, pwd):
    if usern in users and users[usern][0] == pwd:
        print(users[usern][1])
    else:
        print("could not verify")

def emailVerification():
    pass


uname = input("Please enter Username: ")
passwd = input("Please enter password: ")
verify(uname, passwd)
