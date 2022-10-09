class Shoe:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def wear_shoe(self):
        print('I\'m wearing soe')

class Converse(Shoe):
    def __init__(self, color, height, tongue_color):
        super().__init__(color, brand = 'Converse')
        self.height = height
        self. tongue_color = tongue_color


class CombatBoot(Shoe):
    def __init__(self, branch, location):
        super().__init__(color='Green', brand='IBIS')
        self.branch = branch
        self.location = location

converse = Converse('red', 'low', 'yellow')
converse.wear_shoe()
print(dir(converse))