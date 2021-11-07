class Animal:

    def __init__(self, name):
        self.name = name

    def voice(self):
        print('Ahrrrrrgr')

    def say_name(self):
        print(f'My name is {self.name}')


class Dog(Animal):

    def voice(self):
        print('Gav Gav Gav')


class Cat(Animal):

    def voice(self):
        print('Mew Mew Mew')


class Cow(Animal):

    def voice(self):
        print('Mooooooooooo')


unknown = Animal('Noname')
dog = Dog('Zhuchka')
cat = Cat('Abricos')
cow = Cow('Burenka')

animals = [unknown, dog, cat, cow]

for animal in animals:
    animal.say_name()
    animal.voice()
