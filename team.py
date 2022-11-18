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
