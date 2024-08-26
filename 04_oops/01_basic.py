class Car:
    # constructor 
    # __brand for making private
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    
    def get_brand(self):
        return self.__brand + "!"
    def show_brand_and_model(self):
        return f"{self.__brand} {self.model}"
        
 
# incapsulation
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        

my_electric_car = ElectricCar("tesla", "model S", "85kv")
print(my_electric_car.model)
print(my_electric_car.get_brand())
print(my_electric_car.show_brand_and_model())
 
 
 
        
my_car = Car("Tata", "safari")
print(my_car)
print(my_car.get_brand())
print(my_car.model)

print(my_car.show_brand_and_model())
