# Dice Roller #
import random
TotalDice = 10
DieList = []
Die = 1
Difficulty = 9
Specialty = True

print(f"Player rolls {TotalDice}D10 against Difficulty {Difficulty}.")

# Construct the Die List #
while Die <= TotalDice:
    Face = random.randint(1,10)
    DieList.append(Face)
    Die += 1

# Sort the Die List #
DieList.sort()

# Count Ones, Successes, and Tens #
Ones = 0
Succ = 0
BonusDice = 0
# Iterate DieList using indices #
for index in range(len(DieList)):
    if DieList[index] == 1: 
        Ones += 1  # Count Ones
    elif DieList[index] == 10:  # Count Tens
        if Specialty:  # If Specialty Roll, Roll an Extra Die
            Face = random.randint(1, 10)
            if Face >= Difficulty:
                Succ += 1
            DieList.append(Face)
            BonusDice += 1  # Count Bonus Dice
            Succ += 1  # Increment Success Count on a Specialty 10
        else:
            Succ += 1 # Increment Success Count on a non Specialty 10
    elif DieList[index] >= Difficulty:  # Increment Success Count 
        Succ += 1

# Check for Botch (Zero Successes and at least 1 One #
Botch = False
if Ones > 0 and Succ <= 0:
    Botch = True

# Output the Die Results #
BonusPrinted = False
Die = 1
while Die <= TotalDice + BonusDice:
    if Die > TotalDice and Die <= TotalDice + BonusDice:
        if BonusPrinted == False:
            print(f"You rolled {BonusDice} Bonus Dice from Specialty 10's.")
            BonusPrinted = True 
    print(f"Die {Die} has rolled a {DieList[Die-1]}!")    
    Die+= 1
print(f"This Roll has resulted in {Succ} Successes.")
if Botch:
    print("This Results in a BOTCH!")
