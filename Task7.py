class Animal:
    instances_count = 0

    def __init__(self):
        Animal.instances_count = Animal.instances_count + 1

    @staticmethod
    def getInstancesCount():
        print(Animal.instances_count)

    def voice(self):
        pass


class AnimalDog(Animal):
    def voice(self):
        print('Собака - друг человека')

class AnimalsCat(Animal):
    def voice(self):
        print('Кошка гуляет сама по себе')

class AnimalsParrot(Animal):
    def voice(self):
        print('Говорящий попугай')

Sharic = AnimalDog()
Barsic = AnimalsCat()
Kesha = AnimalsParrot()

Animal.getInstancesCount()
