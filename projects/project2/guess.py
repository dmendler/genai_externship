import random

number_to_guess = random.randint(1, 100) # Random number to guess
attempts = 0 # Number of attempts made

while True: 
    num = int(input("Guess the number (between 1 and 100): "))
    attempts += 1

    if num < number_to_guess: # Check if guess is too low
        print("Too low! Try again.")
    elif num > number_to_guess: # Check if guess is too high
        print("Too high! Try again.")
    else: # Correct guess
        print(f"Congratulations! You've guessed it in {attempts} attempts.")
        break
    
    if attempts >= 10: # Breaks loop if more than 10 attempts are made
        print("Game over! Better luck next time.")
        break