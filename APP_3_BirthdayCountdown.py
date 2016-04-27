# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 11:13:48 2016

@author: richard.vuong
"""

import datetime

def header():
    print('------------------------------')
    print('        BIRTHDAY APP')
    print('------------------------------')

def getUserBirthday():
    print('Enter your date of birth: ')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))
        
    birthday = datetime.datetime(year, month, day)
    return birthday

def computeDays(originalDate, now):
    date1 = now
    date2 = datetime.datetime(now.year, originalDate.month, originalDate.day)
    dt = date1 - date2
    days = int(round(dt.total_seconds() / 60 / 60 / 24))
    return days
    
def birthdayInfo(days):
    if days < 0:
        print('Your birthday is in {} days!'.format(-days))
    elif days > 0:
        print('You had your birthday already this year! {} days ago'.format(days))
    else:
        print('Happy Birthday!!!')

def main():
    header()
    bday = getUserBirthday()
    now = datetime.datetime.now()
    numberOfDays = computeDays(bday, now)
    birthdayInfo(numberOfDays)
    
main()
    