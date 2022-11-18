import random

from ability import Ability
from armor import Armor


class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties
        name: string
        starting_health: integer
        current_health: integer
        abilities: list
        armors: list
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()

    def add_ability(self, ability):
        '''Add ability to abilities list'''
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks
        return: total_damage: integer'''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self, incoming_damage):
        pass

    def take_damage(self, damage):
        pass

    def is_alive(self):
        pass

    def fight(self, opponent):
        '''Current hero will take turns fighting the oppenent passed in'''
        random_number = random.randint(0, 1)
        winner = ''
        if random_number == 0:
            winner = self.name
            loser = opponent.name
        elif random_number == 1:
            winner = opponent.name
            loser = self.name
        print(f'{winner} beats {loser}!')
        return winner
