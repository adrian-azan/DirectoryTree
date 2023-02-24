import os
import fileTraverse as ft

inputDirectory = os.getcwd()
outputFile = "Output.txt"

choice = 0
while choice != 4:
    print("1. Change Directory: {}".format(inputDirectory))
    print("2. Change Output: {}".format(outputFile))
    print("3. Scan")
    print("4. Quit")

    try:
        choice = int(input())
    except:
        print("Not an Option")

    if choice == 1:
        inputDirectory = input("Enter Directory Path")
    elif choice == 2:
        outputFile = input("Enter Output File")
    elif choice == 3:
        ft.setUp(outputFile,inputDirectory)
