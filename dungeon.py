"""
Taylor Fettig
Project 3
dungeon.py
(This file holds monsters and items.)

11/08/2023

*This lab was worked on by myself with the only help coming from Professor Langley*

"""

# Generates random numbers
import random

# Creating the Dungeon class
class Dungeon:
    # Initializing all the variables
    def __init__(self, name: str, description: str) -> None:
        self.__name = name
        self.__description = description
        self.__items = []
        self.__monsters = []
        self.__prior = None
        self.__next = None
        self.__monster_list = []
        
        # Loading monster names from 'monster_names'
        with open('./monster_names') as f:
            self.__monster_list = f.readlines()
            
    # This method will randomly choose how many monsters are in the dungeon.
    def generate(self) -> None:
        # Generating random number of monsters between 0 and 4
        num_monsters = random.randint(0, 4)
        # Loop for choosing random monster name
        for i in range(num_monsters):
            # Using rando.choice to pick a random item from the monster list
            name = random.choice(self.__monster_list)
            # Checking to see if monster with that name is already in room
            if not self.monster_in_dungeon(name):
                # New monster object is created with the selected name
                monster = Monster(name)
                # New monster object is added to the list of monsters in the dungeon
                self.__monsters.append(monster)
        
    # This method should loop over the self.__monsters list and see if a monster is in the room
    def monster_in_dungeon(self, name):
        # Looping through monsters list
        for monster in self.__monsters:
            # If monster with given name is in room, return monster
            if monster.get_name() == name:  
                return monster
        return None
    
    # This method creates and returns a string that represents the room.
    def __str__(self):
        # Provides room name and description
        room_info = f"Name: {self.__name}\nDescription: {self.__description}"
        items_str = ""
        # Iterates through items in the dungeon and appends each item name
        for item in self.__items:
            items_str += f"{item.get_name()}, "
    
        if items_str:
            # Remove the trailing comma 
            items_str = items_str[:-2]  
            room_info += f"\nItems: {items_str}"
    
        return room_info
        
    # This method creates a string of monsters that are in the room.
    def __show_monsters__(self):
        # If monsters are in the room, list the monsters and their stats
        if self.__monsters:
            monster_info = "Monsters in the room:\n"
            for monster in self.__monsters:
                monster_info += f"{monster.get_name()}\n"  
            return monster_info
        else:
            return "No monsters (whew!)"
    
    # Getter for monsters
    def monsters(self):
        return self.__monsters

    # Setter for monsters
    def set_monsters(self, monsters):
        self.__monsters = monsters

    # Getter for items
    def items(self):
        return self.__items

    # Setter for items
    def set_items(self, items):
        self.__items = items

    # Getter for prior
    def prior(self):
        return self.__prior

    # Setter for prior
    def set_prior(self, prior_dungeon):
        self.__prior = prior_dungeon

    # Getter for next
    def next(self):
        return self.__next

    # Setter for next
    def set_next(self, next_dungeon):
        self.__next = next_dungeon
    
        
