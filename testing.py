def textList():

    openfile = open("C:\\Users\\User\\Desktop\\readme.txt", "a+")
    openfile.write(input())

    openfile = open("C:\\Users\\User\\Desktop\\readme.txt", "r")
    content = openfile.read()
    print(content)

textList()