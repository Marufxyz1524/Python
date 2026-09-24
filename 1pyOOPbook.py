class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive(self):

        long_name = f"{self.year} {self.model} {self.year}"
        return long_name.title()  

my_new_car = Car("Ferrari","m6",2025)
print(my_new_car.get_descriptive())

    
