
# 1
class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Publication Name: {self.name}")


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print(f"Chief Editor: {self.chief_editor}")



donald_duck_magazine = Magazine(name="Donald Duck", chief_editor="Aki Hyyppä")
compartment_no_6_book = Book(name="Compartment No. 6", author="Rosa Liksom", page_count=192)

donald_duck_magazine.print_information()
print("\n")
compartment_no_6_book.print_information()

#2

from random import randint

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        if speed_change >= 0:
            self.current_speed = min(self.current_speed + speed_change, self.maximum_speed)
        else:
            self.current_speed = max(self.current_speed + speed_change, 0)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def __str__(self):
        return f"| {self.registration_number:12} | {self.maximum_speed:13} | {self.current_speed:12} | {self.travelled_distance:17} |"


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume


if __name__ == "__main__":
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)


    electric_car.accelerate(randint(0, 20))
    gasoline_car.accelerate(randint(0, 20))


    for _ in range(3):
        electric_car.drive(1)
        gasoline_car.drive(1)


    print(f"Electric Car Kilometer Counter: {electric_car.travelled_distance} km")
    print(f"Gasoline Car Kilometer Counter: {gasoline_car.travelled_distance} km")
