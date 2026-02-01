from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def describe(self):
        print("This is an animal.")


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Cow(Animal):
    def make_sound(self):
        return "Moo!"

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.describe()
    print("Sound:", animal.make_sound())
    print("-" * 20)
