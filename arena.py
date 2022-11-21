from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Areana:
    def __init__(self):
        '''Instantiate properties
        team_one: None
        team_two: None
        '''
        self.team_one = list()
        self.team_two = list()

    def create_ability(self):
        '''Prompt for Ability info
        return Ability with user input values'''
        ability_name = input('What is the ability name? ')
        max_damage = int(
            input('What is the max damage this ability can deal? '))
        return Ability(ability_name, max_damage)

    def create_weapon(self):
        '''Prompt for Weapon info
        return Weapon with user input values'''
        weapon_name = input('What is the weapon name?')
        max_damage = int(
            input('What is the max damage this weapon can deal? '))
        return Weapon(weapon_name, max_damage)

    def create_armor(self):
        '''Prompt for Armor info
        return Armor with user input values'''
        armor_name = input('What is the name of the armor? ')
        max_block = int(
            input('What is the max damage this armor can block? '))

    def create_hero(self):
        '''Prompt for Hero info
        return Hero with user input values'''
        hero_name = input('Hero name: ')
        hero = Hero(hero_name)
        add_item = None
        while add_item != '4':
            add_item = input(
                '[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Finish adding items\n\nWhat would you like to do? ')
            if add_item == '1':
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == '2':
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == '3':
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero
