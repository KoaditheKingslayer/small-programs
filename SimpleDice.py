import random

output = ""
while True:
    numDice = int(input("How many Dice would you like to roll? "))
    face = int(input("How many Faces should each die have? [Minimum 1] ")) + 1
    collection = []
    runningTotal = 0
    for i in range(numDice):
        randomValue = random.randrange(1,face)
        collection.append(randomValue)
        runningTotal = runningTotal + randomValue

    for i in collection:
        output = output + str(i) + " "
        
    print(output + f"Total: {runningTotal}")
    
    output = ""

    roll_again = input("Would you like to roll again? (yes/no): ")
    if roll_again.lower() != "yes":
        break
