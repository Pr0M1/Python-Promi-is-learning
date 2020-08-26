myList = []
while True:
    print("Let's make a list: Item " + str(len(myList) +1) +
     " (Or enter nothing to stop.)")
    things = input()
    if things == "":
        break
    elif things in myList: # If its already on the list, the input 
        
        print("It's already on the the list.")
    myList = myList + [things]
print("Your list: ")
for things in myList:
    print(things)
