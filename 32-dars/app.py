from employee import Employees

class Office:
    def __init__(self, name):
        self.name = name
        self.employees = []
        
    
    def __len__(self):
        return len(self.employees)
    
    def __repr__(self):
        return f"-Office: {self.name} ."
    
    def __call__(self, *values):
        if values:
            for value in values:
                self.joinEmployee(value) 
        else:
            return [ e for e in self.employees ]
    
    def __getitem__(self, index):
        return self.employees[index]
    
    def __setitem__(self,index, new):
        self.employees[index] = new
        
    def __add__(self,value):
        if isinstance(value, Office):
            new_office = Office(f"{self.name} {value.name}")
            new_office.employees = self.employees + value.employees
            return new_office
        elif isinstance(value, Employees):
            self.joinEmployee(value)
        else:
            print(f"{type(value)} cannot be added to the Office")
    def joinEmployee(self,*employees):
        for employee in employees:
            if isinstance(employee , Employees):
                self.employees.append(employee)
            else:
                print("Please enter a employee")
                
ecommerce = Office("E-commerce")

user1 = Employees("Samad", "Asadov", "night shift", "Deployers-21", "Fixer", 15 ) 
user2 = Employees("Abdulloh", "Karimov", "day shift", "Coder-7", "Coder as forms")
user3 = Employees("Jasur", "Shokirov", "night shift", "Coder-7", "Coder as data")
user4 = Employees("Asad", "Adhamov", "night shift", "Coder-7", "Coder as data")
user5 = Employees("Zafar", "Qodirov", "night shift", "Coder-7", "Coder as data")
user6 = Employees("Tursun", "Alimov", "night shift", "Coder-7", "Coder as data")

ecommerce.joinEmployee(user1, user2, user3)