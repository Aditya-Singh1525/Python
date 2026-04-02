import random


def play_guess_num():
    """Plays a number guessing game."""

    print("Welcome to the Number Guessing Game!")
    while True:
        try_play = input("Do you want to play? (Yes/No): ").lower()
        if try_play == "yes":
            break
        elif try_play == "no":
            print("No worries! Maybe next time.")
            return  # Exit the function if they don't want to play
        else:
            print("Invalid input! Please enter 'Yes' or 'No'.")

    # Game starts here
    secret_number = random.randint(1, 1000)
    max_attempts = 10  # You can adjust this
    attempts = 0

    print(
        f"\nI'm thinking of a number between 1 and 1000. You have {max_attempts} attempts."
    )

    while attempts < max_attempts:
        attempts += 1
        try:
            user_guess_str = input(
                f"Attempt {attempts}/{max_attempts}: Enter your guess: "
            )

            if not user_guess_str.isdigit():
                print("Invalid input! Please enter a whole number.")
                continue  # Go to the next loop iteration without counting as an actual guess

            user_guess = int(user_guess_str)

            if not (1 <= user_guess <= 1000):
                print("Your guess is out of the 1 to 1000 range. Please try again.")
                continue  # Go to the next loop iteration

            if user_guess == secret_number:
                print(
                    f"\nCongratulations! You guessed the number '{secret_number}' correctly in {attempts} attempts!"
                )
                break  # Exit the game loop
            elif user_guess < secret_number:
                print("Too low! Try a higher number.")
            else:  # user_guess > secret_number
                print("Too high! Try a lower number.")

        except ValueError:
            # This catch is mostly for int() conversion if isdigit() was somehow bypassed
            # or if input was empty (though isdigit() handles that).
            print("Invalid input! Please enter a valid number.")
            continue  # Go to the next loop iteration

    else:  # This 'else' block executes if the loop finishes without a 'break' (i.e., attempts ran out)
        print(f"\nGame Over! You've run out of attempts.")
        print(f"The number I was thinking of was: {secret_number}")

    print("\nThanks for playing!")


# Call the main game function to start
play_guess_num()
