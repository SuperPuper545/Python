from random import choice

bingo = ['a','b','c','d','e',1,2,3,4,5,6,7,8,9,10]
ticket = []

a = 0
while True:
    a += 1
    if a != 3:
        ticket.append(choice(bingo))
    else: break
    
print(f"Билет со значениями: {ticket}. Победный!")

my_ticket = []
c = 0

while True:
    if my_ticket == ticket:
        print("Это победа!")
        print(f"Чо нафик? Понадобилось {c}, чтобы пабедить, ты что шутишь???")
        break
    else:
        c += 1
        for i in range(1, 3):
            my_ticket.append(choice(bingo))
        if my_ticket != ticket:
            print(my_ticket)
            my_ticket.clear()
            print("Неудачная попытка")
