import os, shutil

def txtCheck():
    os.chdir("C:\\Users\\xl4t3\\Desktop")

    for filename in os.listdir():
        if filename.endswith(".txt"):
            openfile = open(filename)
            content = openfile.read()
            print(content)
            openfile.close()


def lookFor():

    for folderName, subfolders, filenames in os.walk("c:\\"):
        print("The Folder is" + folderName)
        print("The subfolders in" + folderName + " are: " + str(subfolders))
        print("The filename in" + folderName + " are: " + str(filenames))
        print()

        for subfolder in subfolders:
            if "fish" in subfolder:
                #os.rmdir(subfolder)
                print("rmdir on" + subfolder)

        for file in filenames:
            if file.endswith(".py"):
                shutil.copy(os.join(folderName, file), os.join(folderName, file + ".backup"))

txtCheck()