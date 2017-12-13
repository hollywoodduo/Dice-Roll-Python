import random
minNumber = 1
maxNumber = 6

rollAgain = "yes"

while rollAgain == "yes" or rollAgain == "y":
    print("Rolling the dice...")
    print("The values are {} and {}".format(random.randint(minNumber, maxNumber), random.randint(minNumber, maxNumber)))
    rollAgain = input("Roll the dice again?")
else:
    print("Game Over")
