import random

from ability import Ability
from armor import Armor
from weapon import Weapon


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
        self.deaths = 0
        self.kills = 0

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

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

    def defend(self):
        total_defense = 0
        for armor in self.armors:
            total_defense += armor.block()
        return total_defense

    def take_damage(self, name, damage):
        '''Updates self.current_health to reflect the damage minus the defense'''
        damage -= self.defend()
        self.current_health -= damage
        # print(f'{name}\'s damage points is {damage}')
        # print(f'{name}\'s current health is {self.current_health})

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not'''
        if self.current_health <= 0:
            return False
        else:
            return True

    def add_kill(self, num_kills):
        '''Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        '''Update self.deaths with num_deaths'''
        self.deaths += num_deaths

    def fight(self, opponent):
        '''Current hero will take turns fighting the oppenent passed in'''
        random_number = random.randint(0, 1)
        winner = ''
        loser = ''
        print(
            f'Fighter: {self.name}; Kills: {self.kills}; Deaths: {self.deaths}')
        print(
            f'Fighter: {opponent.name}; Kills: {opponent.kills}; Deaths: {opponent.deaths}')
        if bool(self.abilities) == False and bool(opponent.abilities) == False:
            print('draw')
        else:
            while self.is_alive() == True and opponent.is_alive() == True:
                opponent_damage = self.attack()
                opponent.take_damage(opponent.name, opponent_damage)
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
                if self.is_alive() == False:
                    self.add_death(1)
                    opponent.add_kill(1)
                elif opponent.is_alive() == False:
                    opponent.add_kill(1)
                    self.add_death(1)
            print(f'{winner} beats {loser}')
            print('Post-match details:')
            print(
                f'Fighter: {self.name}; Kills: {self.kills}; Deaths: {self.deaths}')
            print(
                f'Fighter: {opponent.name}; Kills: {opponent.kills}; Deaths: {opponent.deaths}')
            return winner, self.kills, self.deaths


if __name__ == '__main__':
    hero = Hero('Wonder Woman', 200)
    weapon = Weapon('Lasso of Truth', 90)
    hero.add_weapon(weapon)
    print(hero.attack())
