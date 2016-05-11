# -*- coding: utf-8 -*-
"""
Created on Tue May 10 14:07:48 2016

@author: richard.vuong
"""
import APP_4_JournalSave

def main():
    printHeader()
    runEventLoop()
    
def printHeader():
    print("--------------------------------------")
    print("             JOURNAL APP")
    print("--------------------------------------")
    
def runEventLoop():
    print("What do you want to do with your journal?")
    cmd = 'EMPTY'
    journalName = "default"
    journalData = APP_4_JournalSave.load(journalName)
    
    while cmd != "x": 
        cmd = input("[L]ist entries, [A]dd an entry, E[x]it journal: ")
        cmd = cmd.lower().strip()

        if cmd == "l":
            listEntries(journalData)
        elif cmd == "a":
            addEntry(journalData)
        elif cmd != "x":
            print("Sorry, '{}' isn't a recognised command".format(cmd))
    
    print("Journal closing")
    APP_4_JournalSave.save(journalName, journalData)   
    
def listEntries(data):
    print("Your journal entries: ")    
    entries = reversed(data)
    for index, entry in enumerate(entries):
        print('~~~ [{}] {}'.format(index + 1, entry))
    
def addEntry(data):
    text = input('type your entry, <enter> to exit: ')
    APP_4_JournalSave.addEntry(text, data)

main()
