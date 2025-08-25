
# World of Games (WoG)

World of Games (WoG) is a simple Python console application that allows users to play multiple mini-games with adjustable difficulty levels.  

---

## Features

- Welcome message personalized with your name.
- Choice of three games:
  1. **Memory Game** – A sequence of numbers appears for 1 second, and you must guess it back.
  2. **Guess Game** – Try to guess a number chosen by the computer.
  3. **Currency Roulette** – Guess the value of a random USD amount in ILS.
- Adjustable difficulty from 1 to 5.
- Input validation for numbers and difficulty levels.
- Easy-to-extend project structure for adding new games.

---

## Project Structure

```

WorldOfGames/
│
├── main.py                  # Entry point of the application
├── Live.py                  # Contains welcome() and load\_game()
├── games/                   # Package containing all game implementations
│   ├── MemoryGame.py        # Memory Game logic
│   ├── GuessGame.py         # Guess Game logic
│   └── CurrencyRoulette.py  # Currency Roulette logic
└── utils/                   # Optional: helper functions
└── **init**.py

````

---

## Installation

1. Clone the repository:
```bash
git clone <repository_url>
````

2. Navigate to the project folder:

```bash
cd WorldOfGames
```

3. Make sure you have **Python 3.6+** installed.

---

## Usage

Run the main program:

```bash
python main.py
```

1. Enter your name when prompted.
2. Choose a game by entering its number (1-3).
3. Choose a difficulty level (1-5).
4. Play the selected game according to the instructions.

---

## Example

```
Enter your name: Alice
Hello Alice and welcome to the World of Games (WoG).
Here you can find many cool games to play...

Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS

Enter game number (1-3): 1
Please choose game difficulty from 1 to 5: 3
```

---

## Adding New Games

1. Create a new Python file in the `games/` folder, e.g., `NewGame.py`.
2. Implement a `play(difficulty)` function.
3. Import the new game in `Live.py` and add it to the `load_game()` selection.

---

## License

This project is open-source and free to use under the MIT License.

