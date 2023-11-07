"""
Taylor Fettig
Project 3
item.py
(This file holds the different types of items.)

11/08/2023

*This lab was worked on by myself with the only help coming from Professor Langley*

"""

# Generates random numbers
import random

# Creating the Item class
class Item:
    
    """
     Static variables belong to a class - not objects (instances) of the class. We are storing these as static
     so we don't have a copy of these lists for every Item we make.
    """
    # Static variable to store condition types
    CONDITIONS = []

    # Static variable to store item types
    ITEMS = []
    
    # Static method to read the file and store in conditions list
    @staticmethod
    def load_conditions():
        with open('./item_attributes') as f:
            Item.CONDITIONS = [line.strip().split() for line in f]
    
    # Static method to read the file and store in items list   
    @staticmethod
    def load_items():
        with open('./item_types') as f:
            Item.ITEMS = f.readlines()
            
            
    # Initialization of Item class       
    def __init__(self, attributes) -> None:
        self.__name = attributes[1]
        self.__condition = random.choice(Item.CONDITIONS)
    
    # Getter for name  
    def name(self):
        return self.__name

    # Getter for condition
    def condition(self):
        return self.__condition[0]

    # Getter for description (condition and name)
    def description(self):
        return f"{self.__condition[0]} {self.__name}"
        
# Creating the Armor class that inherits from Item
class Armor(Item):
    def __init__(self, attributes) -> None:
        super().__init__(attributes)
        # attributes[3] multiplied by the item's condition, converted to an integer.
        # Adds 1 so it isn't deducted, converts to an int
        self.__added_defense = int(float(attributes[3]) * (1 + self.__condition[1]))
     
    # Getter for added_defense   
    def get_added_defense(self):
        return self.__added_defense
    
    # Setter for added_defense
    def set_added_defense(self, added_defense):
        self.__added_defense = added_defense
        
# Creating the Weapon class that inherits from Item
class Weapon(Item):
    def __init__(self, attributes) -> None:
        super().__init__(attributes)
        # attributes[2] multiplied by the item's condition, converted to an integer.
        # Adds 1 so it isn't deducted, converts to an int
        self.__added_attack = int(float(attributes[2]) * (1 + self.__condition[1]))

    # Getter for added attack
    def get_added_attack(self):
        return self.__added_attack
    
    # Setter for added attack
    def set_added_attack(self, added_attack):
        self.__added_attack = added_attack
        
        
