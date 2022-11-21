import random


class Team:
    '''
    Team class does not inherit hero, rather contains Hero objects
    This concept is known as "aggregation" in OOP
    Initialize a team with its name and empty list of heroes
    '''

    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        '''Removes hero from list. If hero not found, return 0'''
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
            else:
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console'''
        for hero in self.heroes:
            print(hero.name)

    def stats(self):
        '''Print team stats'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f'{hero.name} Kill-Death ratio: {kd}')

    def revive_heroes(self, health=100):
        '''Reset all heroes health to starting health'''
        # TODO: for each hero in self.heroes, set hero's current_health to starting_health
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        '''Battle each team against each other'''
        living_heroes = list()
        living_opponents = list()
        for hero in self.heroes:
            living_heroes.append(hero)
        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            fighter_one = random.choice(living_heroes)
            fighter_two = random.choice(living_opponents)
            winner = fighter_one.fight(fighter_two)
            if (winner == fighter_one):
                living_opponents.remove_hero(fighter_two)
            elif (winner == fighter_two):
                living_heroes.remove_hero(fighter_one)
            if len(living_heroes) == 0:
                winning_team = living_opponents.name
            elif len(living_opponents) == 0:
                winning_team = living_heroes.name
        print(f'{winning_team} are the winners!')
        return winning_team
