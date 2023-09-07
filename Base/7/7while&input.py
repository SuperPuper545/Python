'''message = input("Tell me something, and I will erpeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}! Glad to see you")

prompt = "If you tell us who are you, we can pesonalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}! Glad to see you")

age = input("How old are you? ")
age = int(age)
print(age)

height  = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else: print("\nYou'll be able to ride when you're a little older.")

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else: print(f"\nThe number {number} is odd.")

question = input("Я смотрю ты хорошо.. Как у тебя дела? ")
print(f"Хаха! Мне нет никакого дела до твои дел, {question} они у тебя или ещё как-то..")

table = input("Мисье, на сколько персон вам нужен столик? ")
table = int(table)

if table > 8:
    print(f"Извините.. Столика на {table} человек у нас сейчас нету..")
else: print(f"У нас как раз осободился столик на {table} человек. Пройдёмте")

number = input("Ну давай, спроси число, а я тебе скажу, кратно оно 10 или нет: ")
number = int(number)

if number % 10 == 0:
    print(f"\nЧисло {number} кратно десяти.")
else: print(f"\nЧисло {number} не кратно десяти.")

current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else: print(message)

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

prompt = "Желаете приобрести билет."
prompt += "\nНазовите ваш возраст: "
while True:
    age = input(prompt)
    age = int(age)
    if age <= 3:
        print("Господин, вам бесплатно.")
    elif 3 <= age <= 12:
        print("Билет для вас, обойдётся всего в 10$.")
    elif 13 <= age <= 100:
        print("С вас 12$.")
    else:
        print("Чо нафик?")
        break
        
# Начинаем с двух списков: пользователей для проверки
# и пустого списка для хранения проверенных пользователей.
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
# Проверяем каждого пользователя, пока остаются непроверенные
# пользователи. Каждый пользователь, прошедший проверку,
# перемещается в список проверенных.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Вывод всех проверенных пользователей.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses = {}
#Установка флага продолжения опроса.
polling_active = True
while polling_active:
    #Запрос имени и ответа пользователя.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    #Отвтет сохраняется в словаре.
    responses[name] = response
    #Проверка продолжения опроса
    repeat = input("Would you like to let anither person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
#Опрос завершён, вывести результаты.
print("\n--- Poll Result ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")
#Da...
sandwich_orders = ['pastrami','tuna','classic','pastrami','double chesse','pastrami']
finished_sandwich = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("Sorry, pastrami is over")
while sandwich_orders:
    current_sandwitch = sandwich_orders.pop()
    print(f'I made your {current_sandwitch.title()} sandwitch')
    finished_sandwich.append(current_sandwitch)
print("--- Finished sandwitch ---")
for san in finished_sandwich:
    print(san.title())'''

responses = {}
polling_active = True
while polling_active:
    name = input("Введите ваше имя: ")
    response = input("Где бы вы хотели провести отпуск? ")
    responses[name] = response
    repeat = input("За вами есть очередь? (да/нет)")
    if repeat == 'нет':
        polling_active = False
print(responses)
print("--- Результаты опроса ---")
for name, response in responses.items():
    print(f"{name}, хотел бы провести отпуск в {response}.")
