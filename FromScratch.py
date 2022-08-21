import random

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
            print("Your weight in Lbs is: ", cal_kg_to_lbs)
        elif kg_or_lbs.upper() == "L":
            cal_lbs_to_kg = weight * 0.45
            print("Your weight in Kg is: ", cal_lbs_to_kg)

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

def account_name():

    while True:

        name_given = input()

        if len(name_given) < 3:
            print("Name must be more then 3 characters:")
        elif len(name_given) >= 50:
            print("Name cant be more then 50 characters")
        elif name_given == "break":
            break
        else:
            print("Name looks good!")

def car_simulator():

    started = False
    order = ""

    while True:

        order = input("> ").lower()

        if order == "start":
            if started == True:
                print("Car already started.")
            else:
                started = True
                print("The car started.")

        elif order == "stop":
            if not started == True:
                print("Car already stopped.")
            else:
                started = False
                print("The car stopped.")

        elif order == "help":
            print("""
    start - it will start the car.
    stop  - it will stop the car.
    quit  - it quits the program.
            """)
        elif order == "quit":
            break
        else:
            print("I dont understand.")

def nextloop_test():

    numbers = [1, 1, 1, 1, 7]

    for x_count in numbers:
        output = ""
        for count in range(x_count):
            output += "x"
        print(output)

def find_greatest_number():

    numbers = [1, 2, 3, 8, 4, 5]
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    print(max)

def traffic_lights_selfm():
    
    red_light = ()
    yellow_light = ()
    green_light = ()
    
    while True:
             
        if red_light == False:
            print("Its red.")
            red_light = True
            green_light = False

        elif red_light:
            print("Its turning from red.")
            yellow_light = True

            while True:
                
                if green_light:
                    print("Its green!")
                    red_light = False
                    break
                    
                elif yellow_light:
                    print("Its red and yellow.")
                    green_light = True
  
        else:
            red_light = False

def list_testing_selfm():

    my_list = []

    while True:

        item = input("Put something in the list: ")
        
        if item not in my_list:
            my_list.append(item)
            print(my_list)

        elif item in my_list:
            my_list.append(item)
            print("""

Its already on the list. 
Do you want to remove it?
(Y) Yes (N) No

            """, my_list)

            while True:

                answer = input()

                if answer.lower() == "y":
                    my_list.remove(item)
                    print(my_list)
                    break

                elif answer.lower() == "n":
                    break

                else:
                    print("Give my an answer.")
            
def dictionarie():

    phone = input("Phone: ")

    digits_mapping = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four"
    }
    output = ""
    for ch in phone:
        output += digits_mapping.get(ch, "!") + " "
    print(output)

def dictionarie_practice(message):

    words = message.split(" ")
    emojis = {
        ":)": "Fucking",
        ":(": "Fuck..."
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

    words = input()
    print(dictionarie_practice(words))

def how_to_handle_errors():

    try:
        age = int(input("Age: "))
        income = 2000
        risk = income / age
        print(age)
    except ZeroDivisionError:
        print("Age cannot be 0.")
    except ValueError:
        print("Invalid value")

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

    #point1 = Point(10, 20)
    #print(point1.x)

class Mammal:

    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def be_annoying(self):
        print("Lovely")

class Dice:

    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second

    #dice = Dice()
    #print(dice.roll()


