import tkinter as tk
import fileTraverse as ft
import os




window = tk.Tk()
tk.Label(window,text="Directory").grid(row=0)
tk.Label(window,text="Output File").grid(row=1)
inputDirectory = tk.Entry(window)
outputDirectory = tk.Entry(window)

outputFileName = outputDirectory.get()
inputDirectoryName = inputDirectory.get()
scanBtn = tk.Button(window,text="scan directory",
                    command= lambda arg1=outputFileName, arg2=inputDirectoryName:
                    ft.setUp(arg1,arg2))



inputDirectory.grid(row=0,column=1)
outputDirectory.grid(row=1,column=1)
scanBtn.grid(row=2,column=0)
window.rowconfigure(0,weight=1)

window.mainloop()
