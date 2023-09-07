'''with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#file_path = '/home/ehmatthes/other_files/text_files/имя_файла.txt'
#with open(file_path) as file_object:

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input('Введите день рожденя, в формате mmddyy: ')
if birthday in pi_string:
    print('Твой день рождения встречается в числе пи!')
else:
    print('Твой день рождения не встречается в числе пи.(ботяра сука)')
print(f"{pi_string[:52]}...")
print(pi_string)

filename = 'learning_python.txt'

with open(filename) as file_object:
    #for line in file_object:
        #print(line.rstrip())
    #contents = file_object.read()
    #print(contents)
    message = "In Python you can write your programms"
    message.replace("Python", "C#")
    lines = file_object.readlines()
    
string = ''
for line in lines:
    string += line
    
print(string)
print(string.replace("Python", "C#"))
#print(len(string))

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")'''

while True:
    a = input("What's your name? pres 'q' to exit - ")
    if a == 'q':
        break

    filename = 'guest_book.txt'

    with open(filename, 'a') as file_object:
        file_object.write(f"{a}\n")
