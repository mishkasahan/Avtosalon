class Car:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def display_info(self):
        print(f"Car: {self.marka} {self.model}")

class Sedan(Car):
    def __init__(self, marka, model, count_doors):
        super().__init__(marka, model)
        self.count_doors = count_doors

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.count_doors}")

class SUV(Car):
    def __init__(self, marka, model, count_seats):
        super().__init__(marka, model)
        self.count_seats = count_seats

    def display_info(self):
        super().display_info()
        print(f"Seats: {self.count_seats}")

class SportsCar(Car):
    def __init__(self, marka, model, max_speed):
        super().__init__(marka, model)
        self.max_speed = max_speed

    def display_info(self):
        super().display_info()
        print(f"Max Speed: {self.max_speed} km/h")


sedan = Sedan("Toyota", "Camry", 4)
suv = SUV("Ford", "Explorer", 7)
sports_car = SportsCar("Ferrari", "488 GTB", 330)
sedan.display_info()
print("-------------------------")
suv.display_info()
print("-------------------------")
sports_car.display_info()
