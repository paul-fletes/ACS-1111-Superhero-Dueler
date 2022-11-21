from ability import Ability
import random


class Weapon(Ability):
    '''
    This method returns a random value
    between one half to the full attack power of the weapon
    '''

    def attack(self):
        divided_number = int(self.max_damage / 2)
        random_int = random.randint(divided_number, self.max_damage)
        return random_int
