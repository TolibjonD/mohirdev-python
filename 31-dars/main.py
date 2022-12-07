from avto import Avto
from employee import Employees

avto1 = Avto("GM", "Nexia 3", "White", 2022, 1000, 1000)
avto2 = Avto("GM", "Malibu", "Black", 2022, 4000, 1200)
avto3 = Avto("GM", "Damas", "White Summit", 2022, 8000, 3300)
print(Avto.getCount())


# Employess
samad = Employees("Samad", "Asadov", "night shift", "Deployers-21", "Fixer")
print(samad.getAmount())