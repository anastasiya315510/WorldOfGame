import random


def generate_number(difficulty):
    number = random.randint(1, difficulty)
    print(f"number is: {number}")
    return number



def get_guess_from_user(difficulty):
    print(f"Please, enter a secret number between 1 and {difficulty}:")

    while True:
        try:
            secret = int(input())  # Convert input to integer
            if 1 <= secret <= difficulty:  # Check range
                return secret  # Valid input, return it
            else:
                print(f"Please enter a number from 1 to {difficulty}.")
        except ValueError:
            print(f"Invalid input. Please enter a number from 1 to {difficulty}.")




def compare_results(difficulty):
    secret_number = generate_number(difficulty)  # Generate the secret number
    guess_number = get_guess_from_user(difficulty)  # Ask user for guess
    if secret_number == guess_number:
        print("You won!")
    else:
        print("You lost!")


def play(difficulty):
    compare_results(difficulty)




