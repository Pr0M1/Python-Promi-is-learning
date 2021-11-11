import os

def txtCheck():
    os.chdir("C:\\Users\\User\\Desktop")

    for filename in os.listdir():
        if filename.endswith(".txt"):
        #os.unlink(filename) # Dry run
            print(filename)

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
lookFor()