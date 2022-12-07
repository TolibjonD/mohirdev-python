# Birinchi topshiriq Avto klass
class Avto:
    def __init__(self , model, color, price, transmission):
        self.model = model
        self.color = color
        self.price = price
        self.transmission = transmission
        self.mileage = 0

    def getInfo(self):
        info = f"{self.model} has color {self.color} ."
        info += f"Transmission is {self.transmission} and price: $ {self.price} /- ."
        info +=f" Mileage: {self.mileage} km "
        return info
    
    def updateMileage(self, distance):
        self.mileage += distance

    def converterMoney(self):
        result = f"Uzb so'm:  {self.price * 11333,55} so'm"
        return result
# Avto klassdan ob'ekt yaratib olamiz
Nexia = Avto("Nexia" , "White Summit" , 10000 , "Automatic")

        