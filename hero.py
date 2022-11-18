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


if __name__ == '__main__':
    # my_hero = Hero('Grace Hopper', 200)
    # my_hero.fight()
    # wonder_woman = Hero('Wonder Woman', 200)
    # dumbledore = Hero('Dumbledore', 150)
    # wonder_woman.fight(dumbledore)
    # wonder_woman.add_ability(ability='lasso')
    # print(wonder_woman.abilities)
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
