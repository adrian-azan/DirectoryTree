import os
import csv

def setUp(outputFileName,directory):
    if outputFileName[-4:] != '.txt':
        outputFileName += ".txt"

    try:
        os.chdir(directory)
    except:
        print("Could not change directory")
        print(directory)
        return

    try:
        with open(outputFileName,"w", newline= '',encoding='utf-8') as file:
            csvWriter = csv.writer(file)

            os.chdir(directory)
            printFilesCSV(csvWriter,0)
            #printFilesTree(file,0)
            
    except Exception as e:
        print(e)

def printFilesCSV(outputFile, level):
    
    folders = list()
    files = list()
    for value in os.listdir():
        if os.path.isdir(value):
            folders.append(value)
        elif value.lower().endswith(".py"):
            files.append(value)

    for file in files:
        outputFile.writerow([os.getcwd(),file])

    for folder in folders:
        os.chdir(os.getcwd() + "\\" + folder)
        printFilesCSV(outputFile, level + 1)
        os.chdir('..')

def printFilesTree(outputFile,level):

    folders = list()
    files = list()
    for value in os.listdir():
        if os.path.isdir(value):
            folders.append(value)
        else:
            files.append(value)

    for file in files:
            outputFile.write(('\t'*level)+file+'\n')

    for folder in folders:
        outputFile.write(('\t'*level)+folder+":\n")
        
        os.chdir(os.getcwd()+"\\"+folder)
        printFilesTree(outputFile, level+1)
        os.chdir('..')
            


