import random
chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-_+=!@#$%^&*()[]{}<>,.?/:\"'"

def password_generator():
    number = int(raw_input("How many passwords to you want to create? "))
    length = int(raw_input("What do you want the length of your password to be? "))
    if number > 1:
        print "Here are your passwords."
    else:
        print "Here is your password."
    for i in range(number):
        password = ""
        for i in range(length):
            password += random.choice(chars)
        print password
password_generator()