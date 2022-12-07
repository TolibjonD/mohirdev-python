class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.fanlar = []
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
    def fanga_yozil(self, fan):
        self.fanlar.append(fan)
        msg = f" Dear {self.ism} you added {fan} in your curriculum"
        return msg
    
    def remove_fan(self, fan):
        if(fan in self.fanlar):
            self.fanlar.remove(fan)
            msg = f" Dear {self.ism} you removed {fan} in your curriculum"
        else:
            msg = f"Dear {self.ism} {fan} doesn't exist in your curriculum"
        return msg

class Fan:
    def __init__(self, name):
        self.name = name
        self.students = 0
        self.members = []

adabiyot = Fan("Adabiyot")
Tolibjon = Shaxs("Tolibjon" , "Saidqodirov" , "AC212121" , 2001)

class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, kafedra, fakultet):
        super().__init__(ism, familiya, passport, tyil)
        self.kafedra = kafedra
        self.fakultet = fakultet

Sattorov = Professor('Abduvali' , "Sattorov" , "AB121212" , 1978, "IAT" , "Informatika")

class Customers(Shaxs):
    def __init__(self, ism, familiya , passport, tyil, userId ):
        super().__init__(ism, familiya, passport, tyil)
        self.userId = userId

    def get_info(self):
        info = f"{self.ism} {self.familiya} customer has {self.userId} ."
        info += f"Passport: {self.passport} ."

    def Age(self, thisYear):
        msg = thisYear - self.tyil
        return msg
    
class Admins(Customers):
    def __init__(self, ism, familiya, passport, tyil, adminId):
        super().__init__(ism, familiya, passport, tyil, userId=None)
        self.adminId = adminId

    def getId(self):
        msg = f"Admin id: {self.adminId}"
        return msg
    
    def prohibitive(self):
        msg = f"{self.ism} admin was banned by Owner"
        return msg

grouper = Admins("Sardor" , "Samadov" , "SE332211" , 1999, "A123ST1")