#! /usr/lib/python2.7
"""An awesome game created by Daniel Miller and Andreas Stassivik while learning Python"""


#import sys #For import, I believe
import random    
#import csv #maybe for character storage, definitely for use in early versions
#import os 
#import console #Not sure where this will fit in 

from classes import *
    
from functions import * #import game functions

#GAME STARTS =================================

welcome() #Welcome to the dungeon!

char = Hero(char_selection(), 100 ) #Assign returns to char_vars list  

while char.getHealth() > 0 : 

        option = int(display_menu(char))

        if option == 1:   
                print 'It\'s time to fight!' 
                char = fight(char) 

        elif option == 2:  
                print 'It\'s time to heal!'
                char = heal(char) 

        elif option == 3: 
                print 'Saving!'
                saveChar(char) 
                quit()
        else:  
                print("\nPlease enter a valid selection") 
                

#Exits while loop - you die! 
print("You have died!") 



