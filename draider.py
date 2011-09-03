#! /usr/lib/python2.7
"""An awesome game created by Daniel Miller while learning Python"""


#import sys #For import, I believe
from random import randint     
#import csv #maybe for character storage, definitely for use in early versions
#import os 
#import console #Not sure where this will fit in 

from classes import * #import game classes
from functions import * #import game functions

#GAME STARTS =================================

welcome()

char = Hero()

char = char_selection(char)

while char['Health'] > 0 : 

        option = display_menu(char)
        if option == 1:   
                fight() 
                display_menu()
        elif option == 2:  
                heal() 
                display_menu()
        elif option == 3: 
                saveChar() 
                quit()
        else:  
                print("\nPlease enter a valid selection") 
                display_menu(char) 

#Exits while loop - you die! 
print("You have died!") 



