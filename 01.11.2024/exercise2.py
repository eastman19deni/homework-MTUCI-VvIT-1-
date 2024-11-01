class Vehicle:
    def __init__(self, make, model):
        self.make = make      
        self.model = model    
    
    def get_info(self):

        return f"Vehicle: {self.make} {self.model}"
    
class Car(Vehicle):
    def __init__(self,make,model,fuel_type):
        super().__init__(make,model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f"Car: {self.make} {self.model}, Fuel Type: {self.fuel_type}"

vehicle = Vehicle("Make" ,"Model")
print(vehicle.get_info())

car = Car ("Tesla", "BMW", "Ford")
print(car.get_info())