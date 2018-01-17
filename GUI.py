# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 08:58:16 2018

@author: Sid
"""

from tkinter import *
import runpy
    #For Subprocess, if there is an error, add shell = True    
    #Runpy was the alternative as nothing seemed to respond using subprocess

def OpenFile():
    runpy.run_path("globalfile.py")    

def OpenScraper():
    #subprocess.run("scraper.py")
    runpy.run_path("scraper.py")

def OpenVisual():
#    subprocess.run("visual.py", shell = True)
    runpy.run_path("visual.py")
    
def OpenDump():
    runpy.run_path("dump.py")
    
def OpenBasic():
#    subprocess.call("basic.py", shell = True)    
    runpy.run_path("basic.py")
    
root = Tk()


topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#label1 = Label(root, text ="Choose the files with the data you want analyzed:")
#button1 = Button(topFrame, text = "Import File", fg="red", command = OpenFile)
button2 = Button(topFrame, text = "Run Scraping on Twitter Data", fg="blue", command = OpenScraper)
button3 = Button(topFrame, text = "Show Visualizations", fg="green", command = OpenVisual)
button4 = Button(bottomFrame, text = "Test Button", fg="purple", command = OpenBasic)
button5 = Button(topFrame, text = "Dump Files", command = OpenDump)

#label1.pack(side=TOP)
#button1.pack(side=TOP)
button5.pack(side=TOP)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


root.mainloop()