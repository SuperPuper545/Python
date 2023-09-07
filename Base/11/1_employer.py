from employeee import Employee

#Определяем атрибуты класса.
name = "Вася"
last_name = "Одетов"
my_employer = Employee(name, last_name)

#Вызываем методы, чтобы убедиться.
my_employer.show_name()
my_employer.show_last_name()

#Метод оклада.
my_employer.give_raise()

