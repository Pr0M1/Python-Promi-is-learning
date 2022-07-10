import random

def whatif():

    press = input()

    if press == "1":
        print("1")
    elif press != "1":
        print("error")

def letsCount():

    count = range(2,5)
    for n in count:
        print(n)

f = input()
if f == "r":
    print("Hello")
else:
    print("Hhowdy")