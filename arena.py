from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena:
    def __init__(self):
        '''Instantiate properties
        team_one: None
        team_two: None
        '''
        self.team_one = list()
        self.team_two = list()

    def create_ability(self):
        '''Prompt for Ability info
        return Ability with user input values'''
        ability_name = input('What is the ability name? ')
        max_damage = int(
            input('What is the max damage this ability can deal? '))
        return Ability(ability_name, max_damage)

    def create_weapon(self):
        '''Prompt for Weapon info
        return Weapon with user input values'''
        weapon_name = input('What is the weapon name?')
        max_damage = int(
            input('What is the max damage this weapon can deal? '))
        return Weapon(weapon_name, max_damage)

    def create_armor(self):
        '''Prompt for Armor info
        return Armor with user input values'''
        armor_name = input('What is the name of the armor? ')
        max_block = int(
            input('What is the max damage this armor can block? '))

    def create_hero(self):
        '''Prompt for Hero info
        return Hero with user input values'''
        hero_name = input('Hero name: ')
        starting_health = input('Starting health: ')
        hero = Hero(hero_name, starting_health)
        add_item = None
        while add_item != '4':
            add_item = input(
                '[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Finish adding items\n\nWhat would you like to do? ')
            if add_item == '1':
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == '2':
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == '3':
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one'''
        num_of_team_members = int(
            input('How many members would you like on Team One?\n: '))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_one.append(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        num_of_team_members = int(
            input('How many members would you like on Team Two?\n: '))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_two.append(hero)

    def team_battle(self):
        '''Battle team_one and team_two together'''
        for hero in self.team_one:
            for opponent in self.team_two:
                hero.fight(opponent)

    def show_stats(self):
        '''Prints team statistics to terminal'''
        print('\n')
        print(self.team_one.name + ' stats: ')
        self.team_one.stats()
        print('\n')
        print(self.team_two.name + ' stats: ')
        self.team_two.stats()
        print('\n')

        team_one_kills = 0
        team_one_deaths = 0
        for hero in self.team_one.heroes:
            team_one_kills += hero.kills
            team_one_deaths += hero.deaths
        if team_one_deaths == 0:
            team_one_deaths = 1
        print(self.team_one.name + ' average K/D ratio was: ' +
              str(team_one_kills/team_one_deaths))
        team_two_kills = 0
        team_two_deaths = 0
        for hero in self.team_two.heroes:
            team_two_kills += hero.kills
            team_two_deaths += hero.deaths
        if team_two_deaths == 0:
            team_two_deaths = 1
        print(self.team_two.name + ' average K/D ratio was: ' +
              str(team_two_kills/team_two_deaths))

        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print('Survived from ' + self.team_one.name + ': ' + hero.name)
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print('Survived from ' + self.team_two.name + ': ' + hero.name)


if __name__ == '__main__':
    game_is_running = True
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input('Play Again? Y or N: ')
        if play_again.lower() == 'n':
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
