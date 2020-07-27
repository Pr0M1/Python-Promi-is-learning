def collatz(number):
    if number % 2 == 0: #even
        number = number // 2
        print(number)
        return number 
    elif number % 2 == 1: #odd
        number = 3 * number + 1
        print(number)
        return number

while True:
    n = input("Type in a number: ")
    while True:
        if n != 1:
            n = collatz(int(n))
        elif n == 1:
            break
