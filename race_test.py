import random
class Car:
    def __init__(self,name):
        self.name = name
    def move(self):
        print(f"The car {self.name} move")
    def choice(self):
    def crashed(self,obstruction):
        print(f"The car {self.name} crashed into a {obstruction}")
class Obstruction:
    def __init__(self,name):
        self.name = name
    def alarm(self):
        print(f"{self.name} obstruction is in front of car")
class Tree(Obstruction):
    def __init__(self):
        super().__init__('Tree')
class Pole(Obstruction):
    def __init__(self):
        super().__init__('Pole')
class Nothing(Obstruction):
    def __init__(self):
        super().__init__('Nothing')
class Game:
    def __init__(self):
        self.car = Car(input())
        self.obstructions = []
    def generate_obstructions(self):
        count_obstruction = random.randint(1,3)
        for i in range(count_obstruction):
            obstruction_type = random.choice([Tree,Pole,Nothing])
            self.obstructions.append(obstruction_type())
    def start(self):
        count=0
        while True:
            self.car.move()
            for i in self.obstructions:
                #i.alarm()
                i.alarm()
                if (str(i.name)=="Nothing"):
                    print("Road is free")
                else:
                    self.car.crashed(i.name)
                    print("Game over")
                    break
            if random.randint(1,10)==10:
                print("You win!")
                break

game = Game()
game.generate_obstructions()
game.start()