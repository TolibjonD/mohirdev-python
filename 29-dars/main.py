# Birinchi topshiriq Avto klass
class Avto:
    def __init__(self , model, color, price, transmission):
        self.model = model
        self.color = color
        self.price = price
        self.transmission = transmission
        self.mileage = 0

    def getInfo(self):
        info = f"The color of {self.model} is {self.color} ."
        info += f"Transmission is {self.transmission} and price: $ {self.price} /- ."
        info +=f" Mileage: {self.mileage} km "
        return info
    
    def updateMileage(self, distance):
        self.mileage += distance

    def Currency(self):
        result = f"Uzb so'm:  {self.price * 11333,55} so'm"
        return result
# Avto klassdan ob'ekt yaratib olamiz
Nexia = Avto("Nexia" , "White Summit" , 10000 , "Automatic")

# Avtosalon nomli class
class Avtosalon:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.cars = [Nexia]
    
    def addCar(self, car):
        self.cars.append(car)
        msg = f"{car.model} have added successfully into cars !..."
        return msg
    
    def showCars(self):
        return [car.getInfo() for car in self.cars]
pokiza = Avtosalon("Pokiza" , "Pop tumani")