myList = []

while True:
    print("Let's make a list: Item " + str(len(myList) +1) +
     " (To check your list type: 'list'. If you wish to stop, type: 'end')")
    things = input()

    if things == "end": # Ends the list
        break

    elif things == "list": # Checking your items on the list
        print(myList)

    elif things not in myList: # Adds to the list.
        myList.append(things)

    elif things in myList: # Removes it from the list if you want to.
        print("Its already on the list. Do you wish to remove it? 'yes' or 'no'")

        while True:
            answer = input()

            if answer == "yes":
                myList.remove(things)
                break

            elif answer == "no":
                break

print("Your list: ")
for things in myList:
    print(things)
