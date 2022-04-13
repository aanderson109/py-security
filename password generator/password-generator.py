# Password Generator w/ User Interface 1.0
# Code for a random password generator that accepts user input about how many special characters,
#   numbers, uppercase letters, and lowercase letters they would like in the password.

import random
import time

special_chars = [33, 35, 63, 64]
uppercase_letters = range(65, 91)
lowercase_letters = range(97, 123)
pass_numbers = range(48, 58)

up = []
low = []
spec = []
num = []

class Password:
    def __init__(self, up_qty=None, low_qty=None, spec_qty=None, num_qty=None):
        self.up_qty = Password.user_choice_upper()
        self.low_qty = Password.user_choice_lower()
        self.spec_qty = Password.user_choice_special()
        self.num_qty = Password.user_choice_numbers()

    def user_choice_upper():
        while True:
            try:
                up_qty = int(input("Please Enter the Amount of Uppercase Letters You Want: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            if up_qty <= 2:
                print("Sorry, the value must be 3 or above.")
                continue
            else:
                return up_qty

    def user_choice_lower():
        while True:
            try:
                low_qty = int(input("Please Enter the Amount of Lowercase Letters You Want: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            if low_qty <= 2:
                print("Sorry, the value must be 3 or above.")
                continue
            else:
                return low_qty

    def user_choice_special():
        while True:
            try:
                spec_qty = int(input("Please Enter the Amount of Special Characters You Want: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            if spec_qty <= 2:
                print("Sorry, the value must be 3 or above.")
                continue
            else:
                return spec_qty

    def user_choice_numbers():
        while True:
            try:
                num_qty = int(input("Please Enter the Amount of Numbers You Want: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            if num_qty <= 2:
                print("Sorry, the value must be 3 or above.")
                continue
            else:
                return num_qty

    def create(self):

        for i in range(self.up_qty):
            up.append(chr(random.choice(uppercase_letters)))

        for i in range(self.low_qty):
            low.append(chr(random.choice(lowercase_letters)))

        for i in range(self.spec_qty):
            spec.append(chr(random.choice(special_chars)))

        for i in range(self.num_qty):
            num.append(chr(random.choice(pass_numbers)))

        password = num + up + low + spec

        def shuffle(list):
            random.shuffle(list)
            return ''.join(list)
        
        shuffle(password)
        print(*password, sep="")

password = Password()
password.create()
