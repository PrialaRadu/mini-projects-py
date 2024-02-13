# Python TicTacToe game
# TicTacToe console game, player X starts first.


def check_win(board, player):
    # All possible winning conditions (lines, rows, diagonals)
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7)]

    # Returns True if a condition is met
    return any(True for a, b, c in win_conditions if (board[a] == board[b] == board[c] == player))


# Prints the board with current values
def print_board(board):
    print(f"""
      1   2   3
    | {board[1]} | {board[2]} | {board[3]} |
  4 | {board[4]} | {board[5]} | {board[6]} | 6
    | {board[7]} | {board[8]} | {board[9]} |
      7   8   9
    """)


# Validates and Handles errors for user placement input
def validate_placement(board, player):
    try:
        placement = int(input(f'Player {player}, enter your placement: '))
        if (placement not in range(1, 10)) or board[placement] == 'X' or board[placement] == 'O':
            print("Invalid placement, chose another one")
        else:
            return placement
    except ValueError:
        print("Type a valid integer")


def tic_tac_toe(board, player='X'):
    while True:
        # Prints the board
        print_board(board)

        # Retrieves and validates the placement value from the current player
        value = validate_placement(board, player)
        board[value] = player

        # Checks if the current player won
        if check_win(board, player):
            print_board(board)
            print(f'Player {player} won!')
            break

        # Checks if there are no more available moves
        elif ' ' not in board.values():
            print_board(board)
            print('Draw')
            break

        # If the current player did not win and the game is not finished, the next player chooses
        player = 'O' if player == 'X' else 'X'


# Starts the TicTacToe game empty values
tic_tac_toe({i: ' ' for i in range(1, 10)})
