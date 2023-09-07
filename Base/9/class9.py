'''class Dog():
    """Базированая собака."""

    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде"""
        print(f"{self.name} rolled over!")

my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.roll_over()

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThis is {self.restaurant_name}, and the type of it's cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant is open")

my_res = Restaurant("Pampeika", "China")
our_res = Restaurant("Bilibirda", "Finland")
a_res = Restaurant("Ahahah", "England")

my_res.describe_restaurant()
my_res.open_restaurant()
our_res.describe_restaurant()
our_res.open_restaurant()
a_res.describe_restaurant()
a_res.open_restaurant()

class User():

    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def describe_user(self):
        print(f"First name: {self.first_name}. \nLast name: {self.last_name}. \nPassword: {self.password}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}. How are you?")

adm_usr = User("Super", "Puper545", "fafafa123321")

adm_usr.describe_user()
adm_usr.greet_user()

class Car():
    """Простая модель автомобиля"""

    def __init__(self,make,model,year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возращает аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Устанавливает на одометре заданное значение.
        При попытке обратной подкрутки изменение отклоняется.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением."""
        if miles < 0:
            print("You can't roll back an odometer!")
        else: self.odometer_reading += miles
    
#my_new_car = Car('audi','a4',2019)
#print(my_new_car.get_descriptive_name())
#my_new_car.odometer_reading = 23
#my_new_car.update_odometer(23)
#my_new_car.read_odometer()   
#my_new_car.update_odometer(1)

my_used_car = Car('subaru','outback',2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(-100)
my_used_car.read_odometer()

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nThis is {self.restaurant_name}, and the type of it's cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant is open")
        
    def read_served(self):
        """Вывод значения обсл."""
        print(f"Number served: {self.number_served}")

    def set_number_served(self, quantity):
        """Задаём кол-во обсл."""
        self.number_served = quantity

    def increment_number_served(self, served):
        """Увелечение кол-ва обсл."""
        self.number_served += served
    
restaurant = Restaurant("Pampeika", "China")

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.number_served = 1
restaurant.read_served()
restaurant.increment_number_served(2)
restaurant.read_served()

class User():

    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name: {self.first_name}. \nLast name: {self.last_name}. \nPassword: {self.password}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}. How are you?")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        while self.login_attempts != 0:
            self.login_attempts -= 1
        print(self.login_attempts)

adm_usr = User("Super", "Puper545", "fafafa123321")

adm_usr.describe_user()
adm_usr.greet_user()
adm_usr.increment_login_attempts()
adm_usr.increment_login_attempts()
adm_usr.reset_login_attempts()

class Car():
    """Простая модель автомобиля"""

    def __init__(self,make,model,year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возращает аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Устанавливает на одометре заданное значение.
        При попытке обратной подкрутки изменение отклоняется.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением."""
        if miles < 0:
            print("You can't roll back an odometer!")
        else: self.odometer_reading += miles

class Battery():
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size = 75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
    
class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобиля."""

    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля.
        """
        super().__init__(make,model,year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nThis is {self.restaurant_name}, and the type of it's cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant is open")
        
    def read_served(self):
        """Вывод значения обсл."""
        print(f"Number served: {self.number_served}")

    def set_number_served(self, quantity):
        """Задаём кол-во обсл."""
        self.number_served = quantity

    def increment_number_served(self, served):
        """Увелечение кол-ва обсл."""
        self.number_served += served

class IceCreamStand(Restaurant):

    def __init__(self, brestaurant_name, cuisine_type):
        super().__init__(brestaurant_name, cuisine_type)
        self.flavors = ['classic','chocolate','cherry']

    def flavors_list(self):
        print(f"It is list of flavors: {self.flavors}")

my_ice = IceCreamStand("Ice land", "Sugar")
my_ice.flavors_list()

class User():

    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name: {self.first_name}. \nLast name: {self.last_name}. \nPassword: {self.password}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}. How are you?")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        while self.login_attempts != 0:
            self.login_attempts -= 1
        print(self.login_attempts)

class Priveleges():

    def __init__(self):
        self.privileges = [
            'delete users', 'add users',
            'show users passwords',
            'do a flip users'
            ]
        
    def show_privileges(self):
        for privilege in self.privileges:
            print(f"You can: {privilege}")

class Admin(User):

    def __init__(self, first_name, last_name, password):
        super().__init__(first_name, last_name, password)
        self.privileges = Priveleges()

usr = Admin("Super", "Puper545", "fafafa123321")
usr.describe_user()
usr.privileges.show_privileges()'''

class Car():
    """Простая модель автомобиля"""

    def __init__(self,make,model,year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возращает аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Устанавливает на одометре заданное значение.
        При попытке обратной подкрутки изменение отклоняется.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением."""
        if miles < 0:
            print("You can't roll back an odometer!")
        else: self.odometer_reading += miles

class Battery():
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size = 75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print(self.battery_size)
        else: print(f"The battery was upgrated")
    
class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобиля."""

    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля.
        """
        super().__init__(make,model,year)
        self.battery = Battery()

'''my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()'''







