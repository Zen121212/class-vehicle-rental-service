class Vehicle:
    def __init__(self, brand, model, year,rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day
    # def display_info(self):
    #     if isinstance(self, Car):
    #         print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self.get_rental_price()}/day")
    #     elif isinstance(self, Bike):
    #         print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}cc, Rental Price:${self.get_rental_price()}/day")
    def calculate_rental_cost(self, days):
        print(f"Rental cost for {self.brand} {self.model} for {days} days: ${self.__rental_price_per_day * days}")
    def get_rental_price(self):
        return self.__rental_price_per_day
    def set_rental_price(self, new_price):
        if new_price > 0:
            self.__rental_price_per_day = new_price
        else:
            print("price must be greater than zero.")
class Car(Vehicle):
    def __init__(self, brand, model, year,seating_capacity,rental_price_per_day):
        super().__init__(brand, model,year, rental_price_per_day)
        self.seating_capacity = seating_capacity
    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rental Price: ${self.get_rental_price()}/day")
class Bike(Vehicle):
    def __init__(self, brand, model, year, engine_capacity,rental_price_per_day):
        super().__init__(brand, model,year, rental_price_per_day)
        self.engine_capacity = engine_capacity
    def display_info(self):
            print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}cc, Rental Price:${self.get_rental_price()}/day")
def show_vehicle_info(vehicle):
    vehicle.display_info()

car_1 = Car("Toyota", "Corolla", 2020,5, 50)
bike_1 = Bike("Yamaha", "R1", 2019,998, 80)
car_1.display_info()
bike_1.display_info()
show_vehicle_info(car_1)
car_1.calculate_rental_cost(3)