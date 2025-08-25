from enum import Enum


class Game(Enum):
    MEMORY = 1
    GUESS = 2
    CURRENCY_ROULETTE = 3


game_descriptions = {
    Game.MEMORY: "Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back",
    Game.GUESS: "Guess Game - guess a number and see if you chose like the computer",
    Game.CURRENCY_ROULETTE: "Currency Roulette - try and guess the value of a random amount of USD in ILS"
}