import hashlib
#Getting Username and Password
# uname = input("Enter Username: ")
# passwd = input("Enter Password: ")
#Dictionary of verified users
users = {"test": ["123", "This is the Secret Message"],
        "test1": ["1234", "This is the Secret Message number 2"]}

def verify(usern, pwd):
    if usern in users and users[usern][0] == pwd:
        print(users[usern][1])
    else:
        print("could not verify")

#verify(uname, passwd)

users = {"test": ["123", "This is the Secret Message"], "test1": ["1234", "This is the Secret Message number 2"]}

def hash(usern, pwd):
    hpass = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
    print(f"Hashed: {hpass}")
    if usern in users and hpass == hashlib.sha256(users[usern][0].encode('utf-8')).hexdigest():
        print(users[usern][1])
    else:
        print("Could not verify")

hash("test", "123")