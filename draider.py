


welcome_msg = """
Welcome to Dungeon Raider!
A game written by Daniel Miller as he learns the Python programming language.

Please follow the prompts and enjoy the game! 
"""

print(welcome_msg)
print("Please select your character name

#Check if this name already exists and then prompt for another name

char = {}
char['Name'] = raw_input ("What is your name?: ")
print("\nWelcome "+char['Name']+", what would you like to do?")

display_menu()


if option == 1: 
	fight() 
elif option == 2: 
	heal()
elif option == 3:
	saveChar()
	quit()
else: 
	print("\nPlease enter a valid selection")
	displayMenu() 

def fight():
	monster = randomMob()
	print("A fight has begun!") 

def randomMob():
	return monster

def heal():
	return heal

def save() :	
        #Check if name already exists

        
	print("Your character has been saved")

def display_menu ():
	menu_ops = """\n 
	1) Find something to fight!
	2) Heal
	3) Save & Quit
	"""
        print(menu_ops)
	option = raw_input("\nPlease select an option:  ")

