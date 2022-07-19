import datetime

def whatif():

    press = input()

    if press == "1":
        print("1")
    elif press != "1":
        print("error")

def calculate(num1, num2):

    product = num1 * num2

    if product <= 1000:
        return product
    else:
        return num1 + num2

def looping():

    while True:

        f = input()

        if f == "1":
            print("Hi")

        elif f == "2":
            print("Howdy")

        else:
            return

def countDown():
    previous_num = 0

    for i in range(1,10):
        x_sum = previous_num + i
        print("Current number", i, "Previous Number", previous_num, "Sum:", i + previous_num)
        previous_num = i

def callString():

    word = input("Enter word:")
    print("Original String:", word)

    size = len(word)

    print("Printing only even index chars")
    for i in range(0, size - 1, 2):
        print("index[", i, "]", word[i])

def removeString(word, n):

    print("Original string:", word)
    x = word[n:]
    return x

def checkIfvalid():
    
    numbers_x = [10, 20, 30, 40, 10]
    numbers_y = [75, 65, 35, 75, 30]

    if numbers_x[0] == numbers_x[4]:
        print(True)
    else:
        print(False)


checkIfvalid()
    
    