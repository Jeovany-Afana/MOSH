class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def accelerate(self):
        print('The car is accelerating')

    def brake(self):
        print('The car is braking')

class ElectricCar(Car):

     def __init__(self,make,model,year,battery_size):
        super().__init__(make,model,year)
        self.battery_size=70

     def battery_charging(self):
         print('The battery is charging')

driver1=Car("Mercedes", "GLE 400", "2020")

driver1.accelerate();