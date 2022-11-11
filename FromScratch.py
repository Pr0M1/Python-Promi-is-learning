class ST():

    def even_or_odd(self, number):

        if number % 2 == 0: #even
            print("The number " + str(number) + " is even")

        elif number % 2 == 1: #odd
            print("The number " + str(number) + " is odd")
    

my_number = input(print("Give me a number: "))

calculate = ST()
calculate.even_or_odd(int(my_number))

