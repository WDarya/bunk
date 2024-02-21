# import random
# class Car:
#     def __init__(self,name):
#         self.name = name
#     def move(self):
#         print(f"The car {self.name} move")
#     def crashed(self,obstruction):
#         print(f"The car {self.name} crashed into a {obstruction}")
# class Obstruction:
#     def __init__(self,name):
#         self.name = name
#     def alarm(self):
#         print(f"{self.name} obstruction is in front of car")
# class Tree(Obstruction):
#     def __init__(self):
#         super().__init__('Tree')
# class Pole(Obstruction):
#     def __init__(self):
#         super().__init__('Pole')
# class Nothing(Obstruction):
#     def __init__(self):
#         super().__init__('Nothing')
# class Game:
#     def __init__(self):
#         self.car = Car('Car 1')
#         self.obstructions = []
#     def generate_obstructions(self):
#         count_obstruction = random.randint(2,3)
#         for i in range(count_obstruction):
#             obstruction_type = random.choice([Tree,Pole,Nothing])
#             self.obstructions.append(obstruction_type())
#     def start(self):
#         while True:
#             self.car.move()
#             for i in self.obstructions:
#                 #i.alarm()
#                 if (i.alarm()=="Nothing"):
#                     print("Road is free")
#                 else:
#                     self.car.crashed(i.name)
#                     print("Game over")
#                     break
#             if random.randint(1,10)==10:
#                 print("You win!")
#                 break
#
# game = Game()
# game.generate_obstructions()
# game.start()

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self):
        self.y += 1

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check_collision(self, car):
        if self.x == car.x and self.y == car.y:
            return True
        else:
            return False

class Rock(Obstacle):
    pass

class Tree(Obstacle):
    pass

class Menu:
    def __init__(self, commands):
        self.commands = commands

    def display_menu(self):
        for command in self.commands:
            print(command)

car = Car(5, 0)
rock = Rock(6, 2)
tree = Tree(4, 3)

menu_commands = ["Move up", "Move down", "Move left", "Move right"]
menu = Menu(menu_commands)

# Пример использования меню
menu.display_menu()

# Проверка столкновения с препятствием
if rock.check_collision(car):
    print("Collision with rock!")
if tree.check_collision(car):
    print("Collision with tree!")
