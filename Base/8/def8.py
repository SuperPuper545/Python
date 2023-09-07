'''def greet_user(username, msg):
    print(f"Hello, {username.title()}. Wtf man? You write: {msg}")
greet_user("Sup_Pup5", "rfwe")

def describe_pet(animal_type = 'cat', pet_name = 'patrik'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet()
describe_pet(pet_name = 'snowjok', animal_type = 'dog')
describe_pet(pet_name = 'bagira')

#ПРИМЕЧАНИЕ Если используется значения по умолчанию, все параметры со значением по умолчанию
#должны следовать после параметров, у которых значений по 
#умолчанию нет. Это необходимо для того, чтобы Python правильно интерпретировал 
#позиционные аргументы.

def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')

def make_shirt(size = 10, text = "text"):
    print(f"\nText on your shirt: {text.title()}, and size your shirt: {size}.")
make_shirt()
make_shirt(size = 20, text = "Nobody Nose")
    
def describe_city(city, country = "russia"):
    print(f"\n{city.title()}, is in {country.title()}")
describe_city("Moscow")
describe_city(city = "Reykjavik", country = "Iceland")

def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi','mcgill')
print(musician)
musician = get_formatted_name('jimi','mcgill','saul')
print(musician)

def build_person(first_name, last_name):
    person = {'first':first_name, 'last':last_name}
    return person
musician = build_person("Saul","Goodman")
print(musician)

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print('\nPlease tell me your name:')
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")
    
def city_country(name_city, country):
    all_data = f"{name_city}, {country}"
    return all_data.title()
data = city_country("moscow","russia")
print(data)
data1 = city_country("helsenki","finland")
print(data1)

def make_album(musician_name, album_name, a =""):
    full = {'musician':musician_name,'album':album_name}
    if a:
        full['a'] = a
    return full
while True:
    print("\nPlease tell me name your musician and him album: ")
    print("(enter 'q' at any time to quit)")
    musician = input("Musician: ")
    if musician == 'q':
        break
    album = input("Album: ")
    if album == 'q':
        break
    song = input("Song: ")
    if song == 'q':
        break
    full_data = make_album(musician, album, song)
    print(f"\nHello, {full_data}")

def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
username =  ['hahha', 'ty', 'margot']
greet_users(username)

def print_models(unprinted_designs, completed_models):
    """ Имитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещается в completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Выводит информацию обо всех напечатанных моделях."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
 
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

def send_messages(unprinted_messages, completed_messages):
    while unprinted_messages:
        current_messages = unprinted_messages.pop()
        print(f"Printing message: {current_messages}")
        completed_messages.append(current_messages)
def sent_messages(completed_messages):
    print("\nThe following messages have been printed:")
    for completed_message in completed_messages:
        print(completed_message)
 
unprinted_messages = ['Hello', 'Hi', 'qq']
completed_messages = []
send_messages(unprinted_messages[:], completed_messages)
sent_messages(completed_messages)
print(unprinted_messages)
print(completed_messages)

def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(14, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers','extra cheese')

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert','einstein', location = 'princeton',field='physics')
print(user_profile)

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('Nikita','Lemeshev', location = 'Ekateringurg',field='Programming(Python)')
print(user_profile)

def make_sandwitch(*toppings):
    print("\nSandwitch list:")
    for topping in toppings:
        print(f"- {topping}")
make_sandwitch('classic', 'hot', 'double')
make_sandwitch('doublebig')

def car(manufacturer, model_name, **car_list):
    car_list['manufacturer'] = manufacturer
    car_list['model_name'] = model_name
    return car_list
car_profile = car('subaru', 'outback', color = 'blue', tow_package = True)
print(car_profile)'''

def make_pizza(size, *toppings):
    print(f'\nMaking a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f"- {topping}")





