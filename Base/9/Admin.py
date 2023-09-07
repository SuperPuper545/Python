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
