


welcome_msg = """
Welcome to Dungeon Raider!
A game written by Daniel Miller as he learns the Python programming language.

Please follow the prompts and enjoy the game! 
"""

print(welcome_msg)
print("Please select your character name")
char['Name'] = raw_input ("What is your name?: ")
print("\nWelcome "+char['Name']+", what would you like to do?")
print("""\n 
1) Find something to fight!
2) Heal
3) Save & Quit
""")

option = raw_input("\nPlease select an option:  ")

if option == 1: 
	fight() 
elif option == 2: 
	heal()
elif option == 3:
	saveChar()
	quit()
else: 
	print("\nPlease enter a valid selection")

def fight() 
	monster = randomMob() 


def randomMob()

def heal()


def save() 


