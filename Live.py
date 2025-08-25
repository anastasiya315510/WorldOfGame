from Game import *

def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).")
    print("Here you can find many cool games to play...")



def load_game():
    print("Loading game...")

    for game in Game:
        print(f"{game.value}. {game_descriptions[game]}")

    print("Please choose game number from 1 to 3: ")

    while True:
        try:
            game_number = int(input())
            if 0 < game_number < 4:
                break
            else:
                print("Please choose a game number from 1 to 3")
        except ValueError:
            print("Please choose a number from 1 to 3")


    print("Please choose game difficulty from 1 to 5: ")
    while True:
        try:
            difficulty = int(input())
            if 0 < difficulty < 6:
                return difficulty
            else:
                print("Please choose a difficulty from 1 to 5")
        except ValueError:
            print("Please choose a number from 1 to 5")










