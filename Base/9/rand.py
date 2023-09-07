from random import randint

my_ticket = [1,3,7,2,3]
count = 1
while my_ticket != [randint(1, 7) for _ in range(5)]:
    count += 1
print(f'Количество итераций {count}')
