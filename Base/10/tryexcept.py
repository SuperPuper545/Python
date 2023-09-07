'''try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide bu 0!")
    except ValueError:
        print("Impossible data... Try again!")
    else: print(answer)


def count_words(filename):
    """Подсчёт приблизительного количества строк в файле."""
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
        #print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['Book.txt', 'learning_python.txt', 'guest_book.txt', '123.txt']
for filename in filenames:
    count_words(filename)

def read_file(filename):
    try:
        with open(filename) as f:
            print(f'{f.read()}\n')
    except FileNotFoundError:
        #print(f"Дурак, файла с именем {filename} нет в этой директории!")
        pass

filenames = ['cats.txt','dogs.txt', 'd.txt']
for filename in filenames:
    read_file(filename)'''
        
def search_words(filename):
    """Подсчёт приблизительного количества строк в файле."""
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.lower().count('the ')
        words
        print(f"The file {filename} has {words} specified words.")

filename = 'Book.txt'
search_words(filename)
