.. _readme:
.. include:: ../README.rst


===========
tic_tac_toe
===========


    The Tic-Tac-Toe code (game.py)  is a Python program that implements a command-line version of the classic game 
    of Tic-Tac-Toe, also known as "Noughts and Crosses." This code defines the core game mechanics, 
    allowing two players to take turns placing their symbols (X and O) on a 3x3 grid. The code provides 
    functions for displaying the game board, checking for a winning condition for either player, determining 
    if the game ends in a draw, and managing the game's turn-based flow. Players take turns providing row and 
    column inputs to place their symbols on the grid. The code also ensures that the game ends when a player 
    wins or when the grid is full, announcing the winner or declaring a draw. It serves as a foundation for 
    playing Tic-Tac-Toe in a text-based interface.



# Tic-Tac-Toe Game

Welcome to the Tic-Tac-Toe project, a classic game of "Noughts and Crosses" implemented in Python. This project is scaffolded using PyScaffold, providing a structured and organized environment for building your Tic-Tac-Toe game.

## Project Structure

The project follows a well-defined directory structure, promoting code organization and consistency. Key elements include:

- `src/`: The source code of the Tic-Tac-Toe game.
- `tests/`: A test suite using pytest for ensuring the game functions correctly.
- `docs/`: A documentation directory that can be expanded to document the game's functionality.
- `requirements.txt`: A file to manage project dependencies.
- `setup.py` and `setup.cfg`: Project configuration files for distribution.
- `.gitignore`: A standard Git ignore file for excluding unnecessary files from version control.
- `README.md`: The main project documentation file.

## Version Control

The project includes Git for version control, enabling you to track changes and collaborate with others effectively.

## Testing

You can run tests for the Tic-Tac-Toe game code using tests/test_tictactoe, ensuring its correctness and reliability.
You can also use 'tox' to run a test of the game code.

## Documentation

There is documentation in game.py describing how the tic_tac_toe game runs.
## Getting Started

To play Tic-Tac-Toe game, follow these steps:

1. Clone this repository to your local environment.
2. Navigate to the project directory.
3. Install project dependencies: `pip install -r requirements.txt`.
4. Open game.py and hit Run
5. In the command line, follow the prompt to enter your row and column positions until a player wins or there is a draw.

## License

This project is released under an open-source license. Please check the `LICENSE` file for details.

---

Feel free to customize this project to meet your specific needs and create a fantastic Tic-Tac-Toe game using this organized and scaffolded structure. Enjoy the development process!



.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
