import random

print("What would you like the max num to be?")
Maxnum = int(input("Number"))

RanNumber = (random.randint(0, Maxnum))

print("I have chosen a number between 1 in"+str(Maxnum))
print("Guess a number")
UserNum = int(input("(Number)"))

while UserNum != RanNumber:
    if UserNum < RanNumber:
        UserNum = int(input("To Low, try again :)"))
    else:
        UserNum = int(input("To High, try again :)"))

print("Good job! You win. The number was: "+str(RanNumber))