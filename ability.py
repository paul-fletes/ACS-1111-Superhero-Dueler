import random


class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        '''Return a value between 0 and max_damage value'''
        random_value = random.randint(0, self.max_damage)
        return random_value


if __name__ == '__main__':
    ability = Ability('Quick Type', 15)
    print(ability.name)
    print(ability.attack())
