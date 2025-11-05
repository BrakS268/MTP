from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self) -> str:
        pass

    def get_info(self) -> str:
        return f"{self.name} ({self.age} лет) - {self.make_sound()}"


class Dog(Animal):
    def make_sound(self):
        return "Гав! Гав!"


class Cat(Animal):
    def make_sound(self):
        return "Мяу! Мяу!"


class Cow(Animal):
    def make_sound(self):
        return "Мууу!"


if __name__ == "__main__":

    animals = [
        Dog("Бобик", 3),
        Cat("Мурка", 2),
        Cow("Зорька", 5)
    ]

    print("Наши животные:")
    for animal in animals:
        print(f"- {animal.get_info()}")

    try:
        animal = Animal("Абстрактное животное", 1)
        pass
    except TypeError as e:
        print(f"\nОшибка при создании абстрактного класса: {e}")
