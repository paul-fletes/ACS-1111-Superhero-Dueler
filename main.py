from hero import Hero
from ability import Ability
from armor import Armor


def battle_arena():
    '''While loop that keeps fight until one player's is_alive returns false'''
    pass


if __name__ == '__main__':
    # wonder_woman = Hero('Wonder Woman', 200)
    captain_america = Hero('Captain America', 200)
    agility = Ability('Agility', 50)
    captain_america.add_ability(agility)
    shield = Armor('Captain America Shield', 10)
    captain_america.add_armor(shield)

    hulk = Hero('Hulk', 200)
    hulk_smash = Ability('Hulk Smash', 50)
    hulk.add_ability(hulk_smash)
    mutated_skin = Armor('Mutated Skin', 10)
    hulk.add_armor(mutated_skin)

    captain_america.fight(hulk)
