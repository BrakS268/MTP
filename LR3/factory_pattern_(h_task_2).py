from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self) -> str:
        pass

    @abstractmethod
    def get_info(self) -> str:
        pass


class Car(Vehicle):
    def drive(self):
        return "Еду на машине по дороге"

    def get_info(self):
        return "Автомобиль - 4 колеса, двигатель"


class Bike(Vehicle):
    def drive(self):
        return "Кручу педали на велосипеде"

    def get_info(self):
        return "Велосипед - 2 колеса, мускульная сила"


class Motorcycle(Vehicle):
    def drive(self):
        return "Несусь на мотоцикле"

    def get_info(self):
        return "Мотоцикл - 2 колеса, мощный двигатель"


class Truck(Vehicle):
    def drive(self):
        return "Везу груз на грузовике"

    def get_info(self):
        return "Грузовик - 6+ колес, для перевозки грузов"


class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type: str) -> Vehicle:
        vehicle_types = {
            "car": Car,
            "bike": Bike,
            "motorcycle": Motorcycle,
            "truck": Truck
        }

        if vehicle_type.lower() in vehicle_types:
            return vehicle_types[vehicle_type.lower()]()
        else:
            raise ValueError(f"Неизвестный тип транспортного средства: {vehicle_type}")


if __name__ == "__main__":

    vehicles_to_create = ["car", "bike", "motorcycle", "truck"]

    for vehicle_type in vehicles_to_create:
        try:
            vehicle = VehicleFactory.create_vehicle(vehicle_type)
            print(f"{vehicle_type.upper()}:")
            print(f"  - {vehicle.drive()}")
            print(f"  - {vehicle.get_info()}\n")
        except ValueError as e:
            print(f"Ошибка: {e}\n")

    try:
        unknown_vehicle = VehicleFactory.create_vehicle("airplane")
    except ValueError as e:
        print(f"Проверка обработки ошибок: {e}")