'''alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

new_points = alien_0['points']
print(f'You just earned {new_points} points!')

print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else: 
	x_increment = 3

alien_0['x_position'] += x_increment
print(f"New position: {alien_0['x_position']}")

alien_0 = {'x_position': 0, 'y_position': 5, 'z_position': 10}
print(alien_0['z_position'])
del alien_0['z_position']
print(alien_0)

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
 
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

Glosariy = {'Compiler': ' it is procces transformations machine code in computing view.'}
print(f"Compiler - {Glosariy['Compiler']}")'''

Human_0 = {'first_name': 'Nikita', 'last_name': 'Lemeshev', 'city': 'Ekaterinburg'}
Human_1 = {'first_name': 'Dadada', 'last_name': 'Soglasiev', 'city': 'Schupchinsk'}
Human_2 = {'first_name': 'Pepepe', 'last_name': 'Pevcov', 'city': 'Agaga'}
people = [Human_0, Human_1, Human_2]
for human in people:
    print(human)

favorite_places = {"David": ['Home','Street'], "Rose": ['Pool','Cinema']}

for name, places_info in favorite_places.items():
    print(f'{name.title()}, likes to walk in: ')
    for places in places_info:
        print(f'\t{places}')

cities = {
    'Ekaterinburg':{
    'country': 'Russia',
    'population': 1500000,
    'fact':'zalupa',
    },
    'Moscow':{
    'country': 'Russia',
    'population': 10000000,
    'fact':'jopnii',
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city}")
    country = f"{city_info['country']}"
    population = f"{city_info['population']}"
    fact = f"{city_info['fact']}"
    print(f"\tCountry of the city: {country.title()}")
    print(f"\tPopulation in city: {population.title()}")
    print(f"\tInteresting info about city: {fact.title()}")
