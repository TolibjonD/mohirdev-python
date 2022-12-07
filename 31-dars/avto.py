from uuid import uuid4

class Avto:
    __count = 0
    def __init__(self,make, model, color, year , price , km=0):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.__km = km
        self.__id = uuid4()
        Avto.__count += 1
    
    @classmethod
    def getCount(cls):
        return cls.__count
    
    def getKm(self):
        return self.__km
    
    def getId(self):
        return self.__id
    
    def addKm(self, km):
        if(km >= 0):
            self.__km += km
            msg = f"Increased {self.model}'s mileage successfully !..."
        else:
            msg = f"It is impossible that reduce the mileage of {self.model} car."
        return msg