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
            guess = input("Guess a whole (Integer) Number between 1 and 100: ")
            guess = int(guess)
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print(f"Invalid input: {guess}. Please enter a valid integer.")

def game():
    # Generate Number
    guessCount = 0
    win = False
    answer = rNumber()
    
    print("New Game.")
    
    while not win:
        try:
            # Inform User to Guess
            guess = makeGuess()
            guessCount += 1

            # Compare Result
            if guess == answer:
                win = True
                print(f"Congratulations! You won in {guessCount} tries!")
            elif abs(guess - answer) <= 10:
                if guess < answer: 
                    print(f"Higher than {guess}")
                elif guess > answer:
                    print(f"Lower than {guess}")
            else: 
                if guess < answer:
                    print(f"Not Even Close. Higher than {guess}.")
                elif guess > answer:
                    print(f"Not Even Close. Lower than {guess}.")
        except ValueError as e:
            print(f"Unexpected error: {e}")
            
while True:
    game()
