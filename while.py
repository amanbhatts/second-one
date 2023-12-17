import random


def number_guessing_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)

    # Set up variables
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print(f"Try to guess the number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        # Get the player's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check if the guess is correct
        if guess == target_number:
            print(
                f"Congratulations! You guessed the correct number ({target_number}) in {attempts + 1} attempts.")
            break
        else:
            # Provide feedback to the player
            if guess < target_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")

        attempts += 1

    if attempts == max_attempts:
        print(
            f"Sorry, you've run out of attempts. The correct number was {target_number}.")


if __name__ == "__main__":
    number_guessing_game()

