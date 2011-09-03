#! /usr/lib/python2.7
"""An awesome game created by Daniel Miller and Andreas Stassivik while learning Python"""


#import sys #For import, I believe
from random import randint     
#import csv #maybe for character storage, definitely for use in early versions
#import os 
#import console #Not sure where this will fit in 

from classes import * #import game classes
from functions import * #import game functions

#GAME STARTS =================================

welcome() #Welcome to the dungeon!

char_vars = char_selection(char) #Assign returns to char_vars list 

char = Hero(char_vars[0], char_vars[1]) #Finally create Hero with name from prompt and 100 HP into the first and second places. 

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



