#! /usr/lib/python2.6

import sys  

def welcome ():
        welcome_msg = """
Welcome to Dungeon Raider!

A game written by Daniel Miller as he learns the Python programming language.

Please follow the prompts and enjoy the game! 
"""
        print(welcome_msg)

def fight():
	monster = randomMob()
	print("A fight has begun!") 

def randomMob():
	return monster

def heal(char):
	print("Your health is currently "+char['Health']+" HP")

        math.random

        print("The health fairy has granted you 
        

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

char = {}

char_selection(char)

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



