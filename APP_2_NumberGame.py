# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 12:14:22 2016

@author: richard.vuong
"""

print('------------------------------')
print('        PSYCHIC TEST')
print('------------------------------')

import random
randomNumber = random.randint(0,100)
userGuess = 'abc'
numberGuesses = 0

while userGuess != randomNumber:
    
    while userGuess is not int:
        try: 
            userGuess = int(input('Guess a number between 0 - 100: '))
            break
        except ValueError:
            print('That is not a number, try again.')
        
    if userGuess < randomNumber:
        print('Too low')
        numberGuesses += 1
    elif userGuess > randomNumber:
        print('Too high')
        numberGuesses += 1
    else:
        print('Correct! You got this in '+str(numberGuesses)+' guesses!')
        break
