# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 13:33:17 2018

@author: Sid
"""
from tkinter.filedialog import askopenfilename


global fileloc
fileloc = askopenfilename()
print(fileloc)