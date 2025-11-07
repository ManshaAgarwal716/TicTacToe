# Command Line Tic Tac Toe Game

A simple command-line implementation of the classic Tic Tac Toe game written in Python.

## Description

This is a two-player Tic Tac Toe game where players take turns marking spaces on a 3x3 grid. The game is played in the command line interface, where players input numbers (1-9) to place their marks (X or O) on the board.

## Features

- Two-player gameplay (X and O)
- Visual grid display using ASCII characters
- Input validation
- Win detection for all possible combinations
- Draw game detection

## How to Play

1. Run the game using Python:
   ```bash
   python tictactoe.py
   ```

2. The game board is numbered from 1 to 9:
   ```
        *       *      
        *       *      
    1   *   2   *   3  
   * * * * * * * * * * *
        *       *      
        *       *      
    4   *   5   *   6  
   * * * * * * * * * * *
        *       *      
        *       *      
    7   *   8   *   9  
   ```

3. Players take turns entering a number (1-9) to place their mark
4. First player to get three in a row (horizontal, vertical, or diagonal) wins
5. Game ends in a draw if all spaces are filled with no winner

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/TicTacToe.git
   ```

2. Navigate to the game directory:
   ```bash
   cd TicTacToe
   ```

3. Run the game:
   ```bash
   python tictactoe.py
   ```

## Game Rules

- Players alternate turns placing X's and O's on the board
- Players must choose an unoccupied space
- The game ends when either:
  - A player gets three marks in a row (horizontal, vertical, or diagonal)
  - All spaces are filled (draw)

## License

This project is open source and available under the [MIT License](LICENSE).
