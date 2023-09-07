import unittest
from employeee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        """Создание работника."""
        name = "Вася"
        last_name = "Одетов"
        self.my_employer = Employee(name, last_name)

    def test_give_default_rise(self):
        """Проверка выдачи стандартного оклада."""
        self.my_employer.give_raise()
        self.assertTrue(5000)

if __name__ == '__main__':
    unittest.main()
