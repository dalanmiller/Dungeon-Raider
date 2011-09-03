"""Functions for the game Dungeon Raider"""
# GAME FUNCTIONS ==============

def welcome():
        welcome_msg = """Welcome to Dungeon Raider!

	A game written by Daniel Miller as he learns the Python programming language.

	Please follow the prompts and enjoy the game!"""
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
        
        #Choose a random mob from a list of tuples that has the monster data.

	return monster

def heal(char):
	print("Your health is currently "+char['Health']+" HP")

        boost = random.randint(0,100) #Assign random number between 0 - 100 to boost

        print("The health fairy has granted you "+boost+" HP")
        
        char['Health'] += boost #Adding boost to current total of the hash of the key for character 'Health'    

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

        #Need to check if inputted text is only alphanumeric characters "".isalnum()     
        #.istoken() might also be helpful instead as it checks for initial capitalized letters in tokens in a string

        char['Name'] = raw_input("What is your name?: ").capitalize()

        return char

