# Snakes and Ladders
## Introduction
Snakes and ladders is a board game that was invented in ancient India. The game is played on a board with some number of spaces (usually 64, 100 or 144) that trail from the starting square and end on the finishing square. The game is played by following these rules:
- A game consists of at least 2 players, who place their playing piece on the starting square.
- Each of the players alternate taking a turn until a player reaches the finishing space and wins the game.
- Turns consist of a player rolling two 6-sided dice and moving their playing piece the indicated number.
- If a player rolls two of the same number on single roll, they roll again and add the previous rolls to the total.
- If a playing piece lands on bottom of a ladder, the playing piece is transported forward to the top of the same ladder.
- If a playing piece lands on the mouth of a snake, the playing piece is transported backward to the tail of the same snake.

## Starting the game
The game is run through a command-line interface. In order to start the game, navigate to the directory where the 'shoots-ladders.py' file is saved and input 'python3 shoots-ladders.py ' into the command line.

## Gameplay
The first prompt will ask how many players want to play, which will require an integer response, and will then require the user to input a name for each player.

The game is simply played by pressing the enter key to simulate rolling the dice until the game ends.

## Design concepts
The program implements randomness, classes and methods.
