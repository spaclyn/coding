currentNum = 1
while currentNum <= 5:
    print(currentNum)
    currentNum = currentNum + 1
print("\n")
#counting more
currentNumber = 0 
while currentNumber < 11:
    currentNumber += 1
    if currentNumber % 2 == 0:
        continue
    print(currentNumber)

#example of infinite and non infinite loops
x = 1
while x <= 5:
    print(x)
    x += 1

#this will loop for forever
#x = 1
#while x <= 5:
#   print(x)