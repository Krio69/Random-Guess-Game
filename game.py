import random

def random_guess_game():
    print("\nWelcome to Random Guess Game")
    print("\nLet's Start")
    
    while True:
        random_number = random.randint(0, 20)  
        attempts = 3  

        for attempt in range(attempts):
            try:
                guess = int(input(f"\nAttempt {attempt + 1}/{attempts}: Guess a number between 0 and 20: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue

            if guess == random_number:
                print("You won!!! You guessed it right!")
                print("Congratulations! You're amazing at guessing!")
                break
            else:
                print("Incorrect guess.")
                
                
                use_hint = input("Would you like a hint? (yes/no): ").strip().lower()
                
                if use_hint == 'yes':
                    if guess < random_number:
                        lower_bound = max(0, guess + 1)
                        print(f"Too low! Try guessing between {lower_bound} and 20.")
                    else:
                        upper_bound = min(20, guess - 1)
                        print(f"Too high! Try guessing between 0 and {upper_bound}.")
                else:
                    print("Try again.")
        else:
            print(f"\nSorry, you're out of attempts! The correct number was {random_number}.")

        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nThank you for playing! Goodbye!")
            break
        
random_guess_game()
