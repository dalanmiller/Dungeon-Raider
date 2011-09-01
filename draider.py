#! /usr/lib/python2.6

import sys
from random import randint     
#import csv 
#import os 
#import console #Not sure where this will fit in 

import classes
import functions

#GAME STARTS =================================

welcome()

char = {'Name':"", 'Health':"" } #Sets up blank new character 

char_selection(char)

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
        else:  print("\nPlease enter a valid selection") 
                display_menu(char) 

#Exits while loop - you die! 
print("You have died!") 



