from random import randint

class Dice:
    def __init__(self, sides=6):
        self.sides = sides;

    def roll(self):
        return randint(1, self.sides);

rollDice = Dice(); #roll a dice 10 times
for i in range(10):
    print("Rolling a 6-sided dice...")
    rollDice = Dice();
    print(rollDice.roll());

rollDice10 = Dice(10); #make a 10 sided dice
# print(rollDice.roll()); #test
for i in range(10):
    rollDice10 = Dice(10);
    print("Rolling a 10-sided dice...")
    print(rollDice10.roll());

rollDice20 = Dice(20); #makes a 20 sided dice
for i in range(10):
    rollDice20 = Dice(20);
    print("Rolling a 20-sided dice...")
    print(rollDice20.roll());
