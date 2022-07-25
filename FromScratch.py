
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

        if something == "asd":
            print("Its a string")
        elif something == int:
            print("Its a intiger.")
        elif something == float():
            print("Its a float.")

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

def weight_calcuulator():

    while True:

        weight = float(input("Weight: "))
        kg_or_lbs = input("(K)g or (L)bs: ")

        if kg_or_lbs.upper() == "K":
            cal_kg_to_lbs = weight / 0.45
            print("Weight in Lbs: ", cal_kg_to_lbs)
        elif kg_or_lbs.upper() == "L":
            cal_lbs_to_kg = weight * 0.45
            print("Weight in Kg: ", cal_lbs_to_kg)

class Person():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is ", self.name)
        print("Im ", self.age, " years old.")

def new_func(Person):
    p1 = Person("John", 36)
    p1.age = 40
    p1.myfunc()

def credit_house():

    while True:

        house_price = 1000000
        credit = input("What is your credit score? ")

        if int(credit) >= 80:
            money_tenpercent = (house_price / 100) * 10
            print("You have to pay ", money_tenpercent, "for 1 mill loan.")

        elif int(credit) < 80:
            money_twelve_percent = (house_price / 100) * 20
            print("You have to pay ", money_twelve_percent, "for 1 mill loan.")
        else:
            print("Give me a number:")

looping()