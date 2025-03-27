from fingerprintController import *

if __name__ == "__main__":
    print("---------------------------")
    print("Please Choose an Option")
    print("1) Enroll Print")
    print("2) Find Print")
    print("---------------------------")
    choice = input("Enter Number: ")
    if choice == "1":
        print("enroll")
        enroll_finger(get_num())
    elif choice == "2":
        print("find")
        get_fingerprint()
    else:
        print("Not Valid")