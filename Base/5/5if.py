'''cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

requested_topping = 'mushroom'

if requested_topping != "anchovies":
	print('Hold the anchovies!')
else: print('Suck my ball"s')

answer = 17

if answer != 42:
	print("That is not the correct answer. Please try again!")

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(f'{user.title()}, you can post a response if you wish.')
else:
	print(f'{user.title()}, get the fuck out in my programs fuckin asshole!')

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

a = 'Пизда арабам'
b = 'Пизда дибилам'
c = 'пизда арабам'

if a == b or a.lower() == c.lower():
	print("Дану нахуй! ПИЗДАБОЛ ЕБАНЫЙ! Ну или я немного сомневаюсь..")
else: print("Ахахааха проебался да? Пизда арабам")


"""age = 12
if age < 4:
	print('Ticket for you 0$')
elif age < 18:
	print("Ticket for you 25$")
else:
	print('Ticket for you 25$')"""

age = 12

if  age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65: 
	price = 20
print(f"Your admission cost is ${price}.")'''

a = 'green'
b = 'yellow'
c = 'red'

print('Try #1')
if a == 'green':
	print('Successful: 5 point')
elif a == 'yellow':
	print('No way! 10 point')
elif a == 'red': 
	print('Wow! 15 point')

print('Try #2')
if b == 'green':
	print('Successful: 5 point')
elif b == 'yellow':
	print('No way! 10 point')
elif b == 'red': 
	print('Wow! 15 point')

print('Try #3')
if c == 'green':
	print('Successful: 5 point')
elif c == 'yellow':
	print('No way! 10 point')
elif c == 'red': 
	print('Wow! 15 point')

print('_____________')

age = 65

if age < 2:
	print("Младенец")
elif 4 > age >= 2:
	print("Малыш")
elif 13 > age >= 4:
	print("Ребёнок")
elif 20 > age >= 13:
	print("Подросток")
elif 65 > age >= 20:
	print("Взрослый")
else: print("Пожилой")

print('_____________')

requested_toppings = ["mushrooms", "green peppers", "extra chesse"]

for requested_topping in requested_toppings:
	if requested_topping == "green peppers":
		print("Sorry, we are out of green peppers rigth now.")
	else: print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

requested_toppings1 = ["s"]
if requested_toppings1:
	for requested_topping1 in requested_toppings1:
		print(f'Adding {requested_topping}.')
	print('\nFinished making your pizza!')
else: print('Are you sure you want a plain pizza?')

print('_____________')

'''names = ['admin', 'jake', 'andry', 'man', 'wow']

if names:
	for name in names:
		if name == 'admin':
			print('Hello admin, would you like to see a status report?')
		else: print(f'Hello {name.title()}, thank you for logging in again') 
else: print("We need to ind some users!")	

current_users = ['admin', 'jake', 'andry', 'man', 'wow']
new_users = ['lox11', 'ja', 'jake', 'name', 'dr']

for new_user in new_users:
	if new_user in current_users:
		print(f'Sry.. your name is already in use {new_user.title()}.')
	else: print(f'Your name is cool, {new_user.title()}')

print(new_users)
print(current_users)

numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
	if number == 1:
		print(f'{number}st')
	elif number == 2:
		print(f'{number}nd')
	elif number == 3:
		print(f'{number}rd')
	else: print(f'{number}th')'''
