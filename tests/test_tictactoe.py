import pytest
from unittest.mock import patch
from tic_tac_toe.game import print_board, check_winner, is_full, play_game

def test_print_board(capsys): # unit test for printing game board
    board = [["X", "O", " "], ["X", "X", "O"], ["O", "X", "O"]]
    print_board(board)
    captured = capsys.readouterr()
    expected_output = "X | O |   \n---------\nX | X | O \n---------\nO | X | O \n---------\n"
    assert captured.out == expected_output



def test_check_winner(): # unit test to check winner
    board_x_wins_row = [["X", "X", "X"], ["O", "X", "O"], ["X", "O", "O"]]
    board_x_wins_col = [["X", "O", "X"], ["X", "X", "O"], ["X", "O", "O"]]
    board_o_wins = [["X", "O", "X"], ["X", "X", "O"], ["O", "X", "O"]]
    board_no_winner = [["X", "O", "X"], ["X", "X", "O"], ["O", "X", " "]]
    assert check_winner(board_x_wins_row, "X") == True
    assert check_winner(board_x_wins_col, "X") == True
    assert check_winner(board_o_wins, "O") == False
    assert check_winner(board_no_winner, "X") == False


def test_is_full(): # unit test to check if board is full
    board_full = [["X", "O", "X"], ["X", "X", "O"], ["O", "O", "X"]]
    board_not_full = [["X", "O", "X"], ["X", "X", "O"], ["O", "X", " "]]
    assert is_full(board_full) == True
    assert is_full(board_not_full) == False

from io import StringIO
import sys

def test_play_game(capsys): # unit test to check functionality of game
    input_values = ["0", "0", "1", "1", "2", "2", "1", "0", "1", "2", "0", "2", "2", "1", "0", "2", "2", "0"]
    expected_output = [
        "  |   |   \n---------\n   |   |   \n---------\n   |   |   \n---------\n",
        "X |   |   \n---------\n   |   |   \n---------\n   |   |   \n---------\n",
        "X |   |   \n---------\n   |   |   \n---------\n   |   |   \n---------\n",
        "X |   |   \n---------\n   | O |   \n---------\n   |   |   \n---------\n",
        "X |   |   \n---------\n   | O |   \n---------\n   |   |   \n---------\n",
        "X |   |   \n---------\n   | O |   \n---------\n   |   | X \n---------\n",
        "X |   |   \n---------\n   | O |   \n---------\n   |   | X \n---------\n",
        "X |   |   \n---------\n O | O |   \n---------\n   |   | X \n---------\n",
        "X |   |   \n---------\n O | O |   \n---------\n   |   | X \n---------\n",
        "X |   |   \n---------\n O | O | X \n---------\n   |   | X \n---------\n",
        "X |   |   \n---------\n O | O | X \n---------\n   |   | X \n---------\n",
        "X |   | O \n---------\n O | O | X \n---------\n   |   | X \n---------\n",
        "X |   | O \n---------\n O | O | X \n---------\n   |   | X \n---------\n",
        "X |   | O \n---------\n O | O | X \n---------\n   | X | X \n---------\n",
        "X |   | O \n---------\n O | O | X \n---------\n   | X | X \n---------\n",
        "X |   | O \n---------\n O | O | X \n---------\n   | X | X \n---------\n",
        "X |   | O \n---------\n O | O | X \n---------\n   | X | X \n---------\n",
        "X |   | O \n---------\n O | O | X \n---------\n X | X | X \n---------\n",
    ]

    sys.stdin = StringIO("\n".join(input_values))
    play_game()
    captured = capsys.readouterr()
    for output in expected_output:
        assert output in captured.out

def test_play_game_draw(capsys): # unit test to check game function if draw
    input_values = ["0", "0", "0", "1", "0", "2", "1", "0", "1", "1", "1", "2", "2", "1", "2", "0", "2", "2"]
    expected_output = [
        "   |   |   \n---------\n   |   |   \n---------\n   |   |   \n---------\n",
        " X |   |   \n---------\n   |   |   \n---------\n   |   |   \n---------\n",
        " X |   |   \n---------\n   |   |   \n---------\n   |   |   \n---------\n",
        " X | O |   \n---------\n   |   |   \n---------\n   |   |   \n---------\n",
        " X | O |   \n---------\n   |   |   \n---------\n   |   |   \n---------\n",
        " X | O | X \n---------\n   |   |   \n---------\n   |   |   \n---------\n",
        " X | O | X \n---------\n   |   |   \n---------\n   |   |   \n---------\n",
        " X | O | X \n---------\n O |   |   \n---------\n   |   |   \n---------\n",
        " X | O | X \n---------\n O |   |   \n---------\n   |   |   \n---------\n",
        " X | O | X \n---------\n O | X |   \n---------\n   |   |   \n---------\n",
        " X | O | X \n---------\n O | X |   \n---------\n   |   |   \n---------\n",
        " X | O | X \n---------\n O | X | O \n---------\n   |   |   \n---------\n",
        " X | O | X \n---------\n O | X | O \n---------\n   |   |   \n---------\n",
        " X | O | X \n---------\n O | X | O \n---------\n   | X |   \n---------\n",
        " X | O | X \n---------\n O | X | O \n---------\n   | X |   \n---------\n",
        " X | O | X \n---------\n O | X | O \n---------\n O | X |   \n---------\n",
        " X | O | X \n---------\n O | X | O \n---------\n O | X |   \n---------\n",
        " X | O | X \n---------\n O | X | O \n---------\n O | X | X \n---------\n",
    ]

    sys.stdin = StringIO("\n".join(input_values))
    play_game()
    captured = capsys.readouterr()
    for output in expected_output:
        assert output in captured.out
    assert "It's a draw!" in captured.out


from tic_tac_toe.game import __version__

def test_version(): # unit test for game version
    # Replace 'expected_version' with the actual version number
    expected_version = "1.0.0"
    assert __version__ == expected_version

if __name__ == "__main__":
    pytest.main(["-v", "--cov=game"])
