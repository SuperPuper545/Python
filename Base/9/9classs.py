from class9 import Car, ElectricCar
#from class9 import ElectricCar as EC

#my_tesla = EC(...)

#import class9 - импортирование всего класса
#from class9 import * - импортирование всего класса из модуля

#my_beetle = car.Car('volkswagen', 'beetle', 2019)
#print(my_beetle.get_descriptive_name())

#my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
#print(my_tesla.get_descriptive_name())

my_new_car = Car('audi','a4',2019)

print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla','model s',2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

'''Иногда классы приходится распределять по нескольким модулям, чтобы избежать 
чрезмерного разрастания одного файла и хранения несвязанных классов в одном 
модуле. При хранении классов в нескольких модулях может оказаться, что один 
класс из одного модуля зависит от класса из другого модуля. В таких случаях необходимый класс можно импортировать в первый модуль.
Допустим, класс Car хранится в одном модуле, а классы ElectricCar и Battery — 
в другом. Мы создадим новый модуль с именем electric_car.py (он заменит файл 
electric_car.py, созданный ранее) и скопируем в него только классы Battery
и ElectricCar:
electric_car.py
 """Набор классов для представления электромобилей."""
 
❶ from car import Car
 
 class Battery():
 ...
 class ElectricCar(Car):
 ...
Классу ElectricCar необходим доступ к классу-родителю Car, поэтому класс Car
импортируется прямо в модуль в точке . Если вы забудете вставить эту команду, 
192 Глава 9 • Классы
при попытке создания экземпляра ElectricCar произойдет ошибка. Также необходимо обновить модуль Car, чтобы он содержал только класс Car:
car.py
"""Простая модель автомобиля."""
class Car():
...
Теперь вы можете импортировать классы из каждого модуля по отдельности и создать ту разновидность машины, которая вам нужна:
my_cars.py
❶ from car import Car
 from electric_car import ElectricCar
 my_beetle = Car('volkswagen', 'beetle', 2019)
 print(my_beetle.get_descriptive_name())
 my_tesla = ElectricCar('tesla', 'roadster', 2019)
 print(my_tesla.get_descriptive_name())
В точке  класс Car импортируется из своего модуля, а класс ElectricCar — из своего. После этого создаются экземпляры обоих разновидностей. Вывод показывает, 
что экземпляры были созданы правильно:
2019 Volkswagen Beetle 
2019 Tesla Roadster'''
