import os
import os.path as OP
import csv
import time

def setUp(outputFilePath,rootDirectory, batch):
    tm = time.localtime()
    outputFile = "Output_{}_{}_{}H{}M{}s.csv".format(tm[1], tm[2], tm[3], tm[4], tm[5])
    try:
        with open(OP.join(outputFilePath,outputFile),"w", newline= '',encoding='utf-8') as outputfile:
            csvWriter = csv.writer(outputfile)
            for i in range(len(batch)):
                print(batch[i:i+5])
            for folder in batch:
                printFilesCSV(csvWriter,0,OP.join(rootDirectory,folder))
            #printFilesTree(file,0)
            
    except Exception as e:
        print(e)

def printFilesCSV(outputFile, level,path):

    folders = list()
    files = list()
    for value in os.listdir(path):
        if OP.isdir(value):
            folders.append(value)
        elif value.lower().endswith(".py"):
            files.append(value)

    for file in files:
        outputFile.writerow([path,file])

    for folder in folders:
        if level == 0:
            print(folder)

        printFilesCSV(outputFile, level + 1,OP.join(path,folder))


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
            


