"""
Taylor Fettig
Project 3
character.py
(This file holds the different types of characters.)

11/08/2023

*This lab was worked on by myself with the only help coming from Professor Langley*

"""

# Generates random numbers
import random

# Creating the Item class
class Character:
    def __init__(self, name):
        # Testing to see if name is blank
        if not name:
            raise ValueError("Name cannot be blank")
        
        self.__name = name
        self.__health = random.randint(50, 100)
        self.__base_attack = random.randint(5, 20)
        self.__base_defense = random.randint(5, 10)
        self.__luck = random.randint(1, 20)
        self.__inventory = []
        self.__armor = []
        self.__weapon = Weapon(("weapon", "Barehanded", 1, 0, 0))
        self.__weapon.set_condition("Normal")
    
    # Getter for name
    def get_name(self):
        return self.__name
     
    # Returns character's name and class  
    def quick_info(self) -> str:
        return f"{self.__name} the {self.__class__.__name__}"
    
    # Getter for health    
    def get_health(self):
        return self.__health
    
    # Setter for health, if health is 0 raises an exception
    def set_health(self, health):
        self.__health = health
        if health <= 0:
            raise CharacterDeathException(f"{self.__name} has died.")
            
    # Returns the inventory list        
    def inventory(self):
        return self.__inventory
     
    # Getter for weapon   
    def get_weapon(self):
        return self.__weapon

    # Setter for weapon
    def set_weapon(self, weapon):
        self.__weapon = weapon
    
    # Getter for armor    
    def get_armor(self):
        return self.__armor

    # Setter for armor, 
    def set_armor(self, armor):
        # Check if a piece of armor with the same name is already in the armor list
        for existing_armor in self.__armor:
            if existing_armor.get_name() == armor.get_name():
                # Move the existing armor to the player's inventory
                self.__inventory.append(existing_armor)
                self.__armor.remove(existing_armor)
                break 
        # Add the new armor to the armor list
        self.__armor.append(armor)
    
    # Search the inventory for the item and return it    
    def in_inventory(self, item_description):
        for item in self.__inventory:
            if item.get_description() == item_description:
                return item
        return None

    # Search the armor list for the item and return it
    def wearing(self, item_description):
        for armor in self.__armor:
            if armor.get_description() == item_description:
                return armor
        return None        
    
    # Getter for base attack 
    def get_base_attack(self):
        return self.__base_attack

    # Setter for base attack
    def set_base_attack(self, base_attack):
        self.__base_attack = base_attack

    # Getter for base defense
    def get_base_defense(self):
        return self.__base_defense
    
    # Setter for base defense
    def set_base_defense(self, base_defense):
        self.__base_defense = base_defense
    
    # Calculate total defense   
    def total_defense(self) -> int:
        # Sum of added defense from armor plus base defense
        total_armor_defense = sum(armor.get_added_defense() for armor in self.__armor)
        return self.__base_defense + total_armor_defense
    
    # Calculate the total attack
    def total_attack(self) -> int:
        weapon_attack = self.__weapon.get_added_attack()
        return self.__base_attack + weapon_attack
    
    # Calculate how much damage a character takes when attacking or being attacked   
    def take_damage(self, enemy) -> int:
        damage = enemy.total_attack() - self.total_defense()
        if damage < 0:
            damage = 0
        # Reduce the character's health
        self.health -= damage
        # Throws an exception if health is below 0
        if self.health <= 0:
            raise CharacterDeathException(f"{self.__name} has died.")
        return damage 
    
    # String representation of character    
    def __str__(self) -> str:
        weapon_str = f"Weapon: {self.__weapon.get_description()}\n"
        # List armor that is worn
        armor_str = "Armor Worn:\n"
        for armor in self.__armor:
            armor_str += f"{armor.get_description()}\n"
        # List of items in inventory
        inventory_str = "Inventory:\n"
        for item in self.__inventory:
            inventory_str += f"{item.get_description()}\n"
        # Character description
        character_str = (
            f"Character: {self.__name}\n"
            f"Class: {self.__class__.__name}\n"
            f"Attack: {self.total_attack()}\n"
            f"Defense: {self.total_defense()}\n"
            f"Luck: {self.__luck}\n"
            f"\n{weapon_str}"
            f"\n{armor_str}"
            f"\n{inventory_str}"
        )
        
        

        return character_str
        
            
