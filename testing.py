import os

def textwrithing():

    userr = input("")
    
    if userr == "d":
        openfile = open("C:\\Users\\User\\Desktop\\readme.txt", "a+")
        openfile.write(input(""))

        openfile = open("C:\\Users\\User\\Desktop\\readme.txt", "r")
        content = openfile.read()
        print(content)