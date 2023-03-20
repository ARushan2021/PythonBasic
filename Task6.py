class Animal:
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

Sharic.voice()
Barsic.voice()
Kesha.voice()

