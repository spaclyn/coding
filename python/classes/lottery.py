from random import choice

class Lottery:
    def __init__(self, numbers):
        self.numbers = numbers;

    def draw(self):
        return choice(self.numbers);

lotteryNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e',];
lotteryDraw = Lottery(lotteryNumbers); #draw a lottery number
#for i in range(4):
#    print("Drawing a Lottery Number...")
#    print(lotteryDraw.draw());

print("If your ticket matched the drawn numbers (or letters), you win!")

#lottery analysis
#myTicket = [1, 2, 3, 'a', 'e']; #how many times did it take to win? (match all 5 numbers)
myMatches = 0;

while myMatches < 5:
    #myTicket = [choice(lotteryNumbers) for i in range(5)]; this made it so that the ticket changes every time, which isn't what I wanted. I need to keep the same time and keep drawing 
    myTicket = [1, 2, 3, 'a', 'e']; #how many times did it take to win? (match all 5 numbers)
    winningNumbers = [lotteryDraw.draw() for i in range(5)];
    for number in winningNumbers:
        if number in myTicket:
            myMatches += 1;
            string = "number" if myMatches == 1 else "numbers";
            print(f"You've Matched {myMatches} {string}!") #print the number of matches after each draw -- need to have it break the loop if it matches all 5 numbers
        else:
            print("No match this time. Keep trying!");

#how many times did it take to win (matched all 5 numbers)?
print(f"Congrats! You've matched all 5 numbers! It took {myMatches} loops to win the lottery!");
#its constantly saying 5, which means that the numbers 





"""matches = 0;
for number in winningNumbers:
    if number in lotteryNumbers:
        matches += 1;

print(f"You've Matched {matches} numbers!");"""