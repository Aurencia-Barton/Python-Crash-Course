#from car import Car, ElectricCar
import car

#my_mustang = Car('ford', 'mustang', 2024)
my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())