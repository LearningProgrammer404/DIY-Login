# Making a user and password login system to start with. Will improve as I go along.

userdirectory = {}


def registration():
    username = input("What would you like your User Name to be? ")
    userpass = input("What would you like your Password to be? ")
    userdirectory[username] = userpass


registration()


def login1():
    userattempt = input("Please Enter your User Name")
    while userattempt not in userdirectory.keys():
        userattempt = input("That is not a valid username, Please try again")
    userpassattempt = input("Please enter your password")
    while userpassattempt != userdirectory[userattempt]:
        userpassattempt = input("Please try another password")

login1()