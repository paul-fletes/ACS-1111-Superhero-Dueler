import random


class Armor:
    def __init__(self, name, max_block):
        '''
        name: string
        max_block: integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        random_value = random.randint(0, self.max_block)
        return random_value


if __name__ == '__main__':
    armor = Armor('Keyboard shield', 20)
    print(armor.name)
    print(armor.block())
