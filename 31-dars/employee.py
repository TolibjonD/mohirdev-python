from uuid import uuid4
class Employees:
    __amount = 0
    def __init__(self , name, lastname, shift, group, rank ,salary=10):
        self.name = name
        self.lastname = lastname
        self.shift = shift
        self.group = group
        self.rank = rank
        self.__salary = salary
        self.__id = uuid4()
        Employees.__amount += 1
        
    def getInfo(self):
        msg = f"Name: {self.name}. Lastname: {self.lastname}. Shift: {self.shift}. "
        msg += f"Group: {self.group}. Job: {self.rank}"
        return msg
    
    @classmethod
    def getAmount(cls):
        return f"Amount of Users: {cls.__amount}"
    
    def getId(self):
        return self.__id
    
    def getSalary(self):
        return f"$ {self.__salary} /-"
    
    def upSalary(self, salary):
        if(salary >= 0):
            self.__salary += salary
            msg = f"{self.name}'s salary increased successfully"
        else:
            msg = "It is injustice to decrease employees' salary !... Please increase ."
        return msg
        