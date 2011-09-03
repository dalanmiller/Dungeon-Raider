# GAME CLASSES ==============

class Organism:
        """Basic attributes for living things in the game"""

        def __init__ (self, name, health):
                self.name = name
                self.health = health
                
        def getName(self):
                return self.name

        def setName(self):
                self.name = self.capitalize()
        
        def getHealth(self):
                return self.health

        def setHealth(self):
                self.health = self

class Hero(Organism):
        """This class provides functions for heroes"""
        #def __init__()
        pass

class Monster(Organism):
        """This class provides functions for monsters"""
        #def __init__()
        pass
