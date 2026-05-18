import random


def guessing_game():
    """Main guessing game function."""
    secret_number = random.randint(1, 100)
    attempts = 0
    min_val, max_val = 1, 100

    print("Welcome to the Guessing Game!")
    print(f"I'm thinking of a number between {min_val} and {max_val}.")
    print("Type 'q' to quit.\n")

    while True:
        user_input = input("What's your guess? ").strip().lower()

        if user_input == 'q':
            print(f"Game over! The number was {secret_number}.")
            break

        try:
            guess = int(user_input)

            if not min_val <= guess <= max_val:
                print(
                    f"Please enter a number between {min_val} and {max_val}.\n")
                continue

            attempts += 1

            if guess == secret_number:
                print(f"\n🎉🎉🎉 CONGRATULATIONS! 🎉🎉🎉")
                print(f"You guessed the number {secret_number}!")
                print(f"You took {attempts} attempt(s). Fantastic job!\n")
                break
            elif guess < secret_number:
                print("Higher!\n")
            else:
                print("Lower!\n")

        except ValueError:
            print("That's not a valid number. Try again.\n")


if __name__ == "__main__":
    guessing_game()
