# Terminal-Based Program. The Computer gives a number, and the player has to try and guess what 
# number it's thinking of. The number will be between 1 and 100 (inclusive). If the guess is wron
# the computer should give a hint about locating the number. The game should continue on until the
# correct guess is made.
import random

# Functions
def rNumber():
    return random.randrange(1, 101)    

def makeGuess():
    while True:
        try:
            guess = int(input("Guess a whole (Integer) Number between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def game():
        # Generate Number
        guessCount = 0
        win = False
        answer = int(rNumber())
        
        print("New Game.")
        
        while win == False:
            # Inform User to Guess
            guess = int(makeGuess())
            guessCount = guessCount + 1

            # Compare Result
            # If guess is equal to answer: Win. Reset Game.
            if guess == answer:
                win = True
                print(f"Congratulations! You won in {guessCount} tries!")
                break  
            # If guess is within 10 of answer, Inform Higher/Lower.
            elif guess <= answer + 10 and guess >= answer - 10:
                if guess < answer: 
                    print(f"Higher than {guess}")
                elif guess > answer:
                    print(f"Lower than {guess}")
                else:
                     break
            # If guess greater than 10 away
            else: 
                    if guess < answer:
                         print(f"Not Even Close. Higher than {guess}.")
                    elif guess > answer:
                         print(f"Not Even Close. Lower than {guess}.")
                    else:
                         break

while True:
    game()
               