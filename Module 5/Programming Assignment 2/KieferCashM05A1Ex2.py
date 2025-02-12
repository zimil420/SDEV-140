import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    
    while True:
        # Generate a random number between 1 and 100
        number_to_guess = random.randint(1, 100)
        
        while True:
            try:
                # Ask the user for a guess
                user_guess = int(input("Guess a number between 1 and 100: "))
                
                if user_guess < 1 or user_guess > 100:
                    print("Out of range! Please guess a number between 1 and 100.")
                    continue
                
                # Check if the guess is too high, too low, or correct
                if user_guess > number_to_guess:
                    print("Too high, try again.")
                elif user_guess < number_to_guess:
                    print("Too low, try again.")
                else:
                    print("Congratulations! You guessed the number!")
                    break  # Exit inner loop to start a new round
            except ValueError:
                print("Invalid input! Please enter a valid number.")

# Run the game
guess_the_number()
