from Live import *
from games.GuessGame import play


def main():
    name = input("Enter your name: ")
    welcome(name)
    difficulty = load_game()
    play(difficulty)

if __name__ == "__main__":
    main()