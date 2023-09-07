from random import randint

class Die():

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        a = randint(1, self.sides)
        print(a)

aa = Die()
bb = Die()
bb.sides = 10
cc = Die()
cc.sides = 20

a = 0
while True:
    if a != 10:
        print("Был брошен кубик с шестью гранями, результат:")
        aa.roll_die()
        print("Был брошен кубик с десятью гранями, результат:")
        bb.roll_die()
        print("Был брошен кубик с двадцатью гранями, результат:")
        cc.roll_die()
    else:
        break
    a += 1
