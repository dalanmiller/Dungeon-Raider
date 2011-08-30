#! /usr/lib/python2.6

import sys, random, csv, os

# GAME FUNCTIONS ==============

def welcome ():
        welcome_msg = """
Welcome to Dungeon Raider!

A game written by Daniel Miller as he learns the Python programming language.

Please follow the prompts and enjoy the game! 
"""
        print(welcome_msg)

#def init():
        #Create csv file if it doesn't exist. 
        #Load items, monsters, characters into memory?
        
        #Pull monsters, weapons, items from public file?

def fight():
        monster = randomMob()
	print("A fight has begun")

        #Pick randomsly from set of monsters
        
        #User gets to engage per round or have random chance at retreating.

def randomMob():
        
        #
	return monster

def heal(char):
	print("Your health is currently "+char['Health']+" HP")

        boost = random.randint(0,100)

        print("The health fairy has granted you "+boost+" HP")
        
        char['Health'] += boost 

        print("Your HP Is now "+char['Health']+" HP")
        
def save() :	
        #Check if name already exists        
	print("Your character has been saved")

def display_menu (char):
        print("\nWelcome "+char['Name']+", what would you like to do?")
	menu_ops = """\n 
	1) Find something to fight!
	2) Heal
	3) Save & Quit
	"""
        print(menu_ops)
	option = raw_input("\nPlease select an option:  ")
        return option

def char_selection(char):
        print("Please select your character name")        
        
        #Check if this name already exists and then prompt for another name      

        char['Name'] = raw_input ("What is your name?: ")

        return char

#GAME STARTS =================================

welcome()

char = {'Name':"", 'Health':"" }

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
        else:  
	        print("\nPlease enter a valid selection")

	        display_menu(char) 

#Exits while loop - you die! 
print("You have died!") 



