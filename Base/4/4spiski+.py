'''magicians = ['alice','david','carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")
print("_____________________")
pizzas = ['mozzarella','chivas','pepperoni']
for pizza in pizzas:
	print(f"I like {pizza.title()} pizza!")
print("Wow! Pizza is so yammi.")
print("_____________________")
for value in range(1,5):
	print(value)
numbers = list(range(1,6))
print(numbers)
event_numbers = list(range(2,11,2))
print(event_numbers)
print("_____________________")
squares = []
for value in range(1,11):
	#square = value**2
	squares.append(value**2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
squares_1 = [value**2 for value in range(1,11)]
print(squares_1)
print("_____________________")
million = [value for value in range(1,1000001)]
print(max(million))
print(min(million))
print(sum(million))
for value in range(1,21,2):
	print(value)
three = [value for value in range(3,30,3)]
cube = [value**3 for value in range(1,11)]
print(cube)
print("_____________________")
players = ['charles','martina','michael','florence','eli']
print(players[1:3])
print(players[-3:])
print(players[:4])
print(players[0:4:2])
print('Here are the first three players on my team:')
for player in players[:3]:
	print(player.title())
print("_____________________")
my_favorite_foods = ['pizza','falafel','carrot cake']
friend_foods = my_favorite_foods[:]
my_favorite_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_favorite_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
print("The irst three items in the list are:")
print(friend_foods[:3])
print("The last three items in the list are:")
print(friend_foods[-3:])
print("The items from the middle of the list are:")
print(friend_foods[1:3])
print("_____________________")
my_pizzas = ['mozzarella','chivas','pepperoni']
friend_pizzas = my_pizzas[:]
my_pizzas.append('supreme pizza')
friend_pizzas.append('bacon pizza')
print("My favorite pizzas are:")
print(my_pizzas)
print("My friend's favorite pizzas are")
print(friend_pizzas)
for value in my_pizzas:
	print(value)
print("_____________________")
dimensions = (200, 50)
print('Original dimensions:')
for dimension in dimensions:
	print(dimension)
dimensions = (400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
	print(dimension)
print("_____________________")
menu = ('fuagra','pizza','spaggetti')
for i in menu:
	print(i)
menu = ('fuagra','pizza','soup')
for i in menu:
	print(i)

user_0 = {
	'username': 'sup_pup5',
	'first': 'enrico',
	'last': 'fermi',
	}
for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

sv1 = ['polo', 'arty', 'man', 'phil']


for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")

for language in set(favorite_languages.values()):
	print(language.title())


Rivers = {'nile': 'egypt', 'mississipi':'usa','yangtze':'japan'}

for rive, country in Rivers.items():
	print(f'The {rive.title()} runs through {country.title()}.')

for rive in Rivers.keys():
	print(rive.title())

for country in Rivers.values():
	print(country.title())


favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

who = ['kevin','jen','edward','phil','jim']
for name in sorted(who):
	if name in favorite_languages:
		print(f'Thank for activity {name.title()}')
	else: print(f'{name.title()}, would you like to take the survey')

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)'''

# Создание пустого списка для хранения пришельцев
aliens = []
# Создание 30 зеленых пришельцев
for alien_number in range(30):
	new_alien = {'color':'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

 # Вывод первых 5 пришельцев:
for alien in aliens[:5]:
	print(alien)
print("...")
# Вывод количества созданных пришельцев
print(f"Total number of aliens: {len(aliens)}")

 # Сохранение информации о заказанной пицце.
pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese'],
 }
 # Описание заказа.
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping)

favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
for name, languages in favorite_languages.items():
	if len(languages) == 1:
		print(f"\n{name.title()}'s favorite language is:")
		for language in languages:
			print(f"\t{language.title()}")
	else: 		
		print(f"\n{name.title()}'s favorite languages are:")
		for language in languages:
			print(f"\t{language.title()}")

users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
 
 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }
 
for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")
