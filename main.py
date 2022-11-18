from hero import Hero
from ability import Ability

if __name__ == '__main__':
    wonder_woman = Hero('Wonder Woman', 200)
    dumbledore = Hero('Dumbledore', 150)
    wonder_woman.fight(dumbledore)
    ability = Ability("Great Debugging", 50)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    print(hero.attack())
