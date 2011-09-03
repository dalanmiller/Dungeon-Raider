#! /usr/lib/python2.7
"""An awesome game created by Daniel Miller and Andreas Stassivik while learning Python"""


#import sys #For import, I believe
from random import randint     
#import csv #maybe for character storage, definitely for use in early versions
#import os 
#import console #Not sure where this will fit in 

from classes import *
    
from functions import * #import game functions

#GAME STARTS =================================

welcome() #Welcome to the dungeon!
vars = char_selection()
char = Hero(vars[0], vars[1] ) #Assign returns to char_vars list  

while char.getHealth > 0 : 

        option = display_menu(char)
        if option == 1:   
                fight() 
                display_menu(char)
        elif option == 2:  
                heal() 
                display_menu(char)
        elif option == 3: 
                saveChar() 
                quit()
        else:  
                print("\nPlease enter a valid selection") 
                display_menu(char) 

#Exits while loop - you die! 
print("You have died!") 



