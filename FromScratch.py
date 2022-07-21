

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
        
        something = input("Type something: ")

        if something == int():
            print("Its a intiger")
        elif something == str():
            print("Its a string.")
        elif something == float():
            print("Its a ")


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

def checkIfvalid(numberList):
    print("Given list:", numberList)

    first_number = numberList[0]
    last_number = numberList[-1]
    
    if first_number == last_number:
        return True
    else:
        False

def simple_calculator():
    

    first_number = float(input("First: "))
    second_number = float(input("Second: "))
    sum = first_number + second_number
    print("Sum: ", sum)

simple_calculator()