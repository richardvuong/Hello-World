# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:13:28 2016

@author: richard.vuong
"""

import os

def load(name):
    data = []
    fileName = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))

    if os.path.exists(fileName):
        with open(fileName) as fin:
            for entry in fin.readlines():
               data.append(entry.rstrip())
                
    return data
    
def save(name, journalData):
    fileName = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    print(".... saving to: {}".format(fileName))
    
    with open(fileName, 'w') as fileOut:
        for entry in journalData:
            fileOut.write(entry + '\n')
        
def addEntry(text, journalData):
    journalData.append(text)
    
