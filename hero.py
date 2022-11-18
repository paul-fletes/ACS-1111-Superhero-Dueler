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

    def add_armor(self, armor):
        '''Add armor to self.armors
        armor: armor object'''
        self.armors.append(armor)

    def defend(self, incoming_damage):
        total_defense = 0
        for armor in self.armors:
            total_defense += armor.block()
        return total_defense

    def take_damage(self, name, damage):
        '''Updates self.current_health to reflect the damage minus the defense'''
        damage -= self.defend()
        print(f'{name}\'s damage points is {damage}')
        self.current_health -= damage
        # print(f'{name}\'s current health is {self.current_health})

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not'''
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        '''Current hero will take turns fighting the oppenent passed in'''
        random_number = random.randint(0, 1)
        winner = ''
        loser = ''
        if bool(self.abilities) == False and bool(opponent.abilities) == False:
            print('draw')
        else:
            while self.is_alive() == True and opponent.is_alive() == True:
                opponent_damage = self.attack()
                opponent.take_damage(opponent.name, opponent.damage)
                self_damage = opponent.attack()
                self.take_damage(self.name, self_damage)
                if self.current_health > opponent.current_health:
                    winner = self.name
                    loser = opponent.name
                else:
                    winner = opponent.name
                    loser = self.name
                self.is_alive()
                opponent.is_alive()
            print(f'{winner} beats {loser}')
        return winner


if __name__ == '__main__':
    #ability = Ability('Great Debugging', 50)
    hero = Hero('Grace Hopper', 200)
    # hero.add_ability(ability)
    # print(hero.attack())
    print(hero.current_health)
    armor = Armor('Debugging Shield', 10)
    hero.add_armor(armor)
    hero.take_damage(50)
    print(hero.current_health)
