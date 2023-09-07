class Employee():

    def __init__(self, name, last_name, s = 0):
        """Сохраняет имя, фамилию и зарплату рабочего."""
        self.name = name
        self.last_name = last_name
        self.salary = s

    def show_name(self):
        """Показать имя рабочего."""
        print(self.name)

    def show_last_name(self):
        """Показать last_имя рабочего."""
        print(self.last_name)

    def give_raise(self):
        """Увеличение ежегодного оклада."""
        a = input("Оставить ежегодный оклад по умолчанию? (да/нет) - ")
        if a == 'да':
            self.salary += 5000
            print(self.salary)
        else:
            b = int(input("Введите необходимую сумму оклада: "))
            self.salary += b
            print(self.salary)
