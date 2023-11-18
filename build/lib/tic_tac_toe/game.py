# Add function to create grid for tic tac toe game
def print_board(board):
    """_summary_

    Args:
        board (_type_): _description_
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# function to define criteria for a player winning
def check_winner(board, player):
    """_summary_

    Args:
        board (_type_): _description_
        player (_type_): _description_

    Returns:
        _type_: _description_
    """
    for row in board:
        if all(cell == player for cell in row): 
            return True # if player fills row, they win

    for col in range(3):
        if all(board[row][col] == player for row in range(3)): 
            return True # if player fills column, they win

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True # if player fills diagonal, they win

    return False

# function to return all full cells in board
def is_full(board):
    """_summary_

    Args:
        board (_type_): _description_

    Returns:
        _type_: _description_
    """
    return all(cell != " " for row in board for cell in row)

# function to output final result based on the game status
def play_game():
    """_summary_
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Enter the row (0, 1, 2) for Player {current_player}: "))
        col = int(input(f"Enter the column (0, 1, 2) for Player {current_player}: "))

        if board[row][col] == " ":
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!") # display when current player wins
                break
            elif is_full(board):
                print_board(board)
                print("It's a draw!") # draw between both players
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("That position is already occupied. Try again.") # if player selects filled position

__version__ = "1.0.0"

if __name__ == "__main__":
    """_summary_
    """
    play_game()

