def collatz(number):
    if number % 2 == 0: #even
        number = number // 2
        return print(number)
    elif number % 2 == 1: #odd
        number = 3 * number + 1
        return print(number)

while True:
    print("Give my a number:")
    number = int(input())
    collatz(number)
    if number != 1:
        collatz(number)