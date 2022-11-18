from hero import Hero
from ability import Ability
from armor import Armor

if __name__ == '__main__':
    wonder_woman = Hero('Wonder Woman', 200)
    dumbledore = Hero('Dumbledore', 150)
    wonder_woman.fight(dumbledore)
    ability = Ability('Great Debugging', 50)
    wonder_woman.add_ability(ability)
    print(wonder_woman.attack())
    armor = Armor('Debugging Shield', 10)
    wonder_woman.add_armor(armor)
    print(wonder_woman.defend())
