"""
Taylor Fettig
Project 3
dungeon.py
(This file holds monsters and items.)

11/08/2023

*This lab was worked on by myself with the only help coming from Professor Langley*

"""

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
        
    # This method should loop overthe self.__monsters list and see if a monster with the given name is in the room. 
    def monster_in_dungeon(self, name) -> Optional[Monster]:
    
    # This method creates and returns a string that represents the room.
    def __str__(self):
        
    # This method creates a string of monsters that are in the room.
    def __show_monsters__(self):
        
    
        
