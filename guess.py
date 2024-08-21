import random

def guess_number():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0
    
    # Start the guessing loop
    while True:
        # Prompt the user to guess the number
        guess = int(input("Guess the number (between 1 and 100): "))
        
        # Increment the attempts counter
        attempts += 1
        
        # Check if the guess is too low, too high, or correct
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            # If the guess is correct, exit the loop
            print(f"Correct! The number was {target_number}.")
            print(f"It took you {attempts} attempts to guess the correct number.")
            break

# Run the game
guess_number()
