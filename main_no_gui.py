import os
import os.path as OP
import fileTraverse as ft
import time

def scanFolders(path="."):
    folders = list()
    for value in os.listdir(path):
        if OP.isdir(OP.join(path,value)):
            folders.append(value)
    return folders




if (OP.isdir("Reports") == False):
    os.mkdir("Reports")

###USER CONTROLLED VALUES
inputDirectory = os.getcwd()
outputDirectory = OP.join(os.getcwd(),"Reports")
outputFile = "Output.csv"
outputFilePath = OP.join(outputDirectory,outputFile)
batch = scanFolders()


choice = 0
while choice != 5:
    print("1. Scan")
    print("2. Set Batches")
    print("3. Change Output: {}".format(outputFilePath))
    print("4. Change Root Directory: {}".format(inputDirectory))
    print("5. Quit")

    try:
        choice = int(input())
    except:
        print("Not an Option")

    if choice == 4:
        possiblyInputDirectory = input("Enter Path for Directory to be Scanned")
        if OP.isdir(possiblyInputDirectory):
            inputDirectory = possiblyInputDirectory
            batch = scanFolders(inputDirectory)
        else:
            print("Failed to scan directory")

    elif choice == 3:
        possibleOutputDirectory = input("Enter Path Output File")
        if OP.isdir(OP.join(possibleOutputDirectory+outputFile)):
            outputFilePath = OP.join(possibleOutputDirectory+outputFile)
        else:
            print("Failed to scan directory")

    # Set Batches
    elif choice == 2:
        batch = scanFolders(inputDirectory)

        for i in range(len(batch)):
            print("{}: {}".format(i, batch[i]))

        start = int(input("Enter Start Folder #"))
        end = int(input("Enter End Folder #")) + 1

        batch = batch[start:end]

    # Scan
    # Scan
    elif choice == 1:
        ft.setUp(outputDirectory,inputDirectory,batch)



