# define functions
import random

from pygame.time import wait
import copy


def print_board(board):
    """
    Prints a string representation of the game board
    :param board: a list of lists representing the game board
    :return: nothing - prints the board
    """

    # declare the board string
    board_string = "\n     |     |     \n  "

    # print the empty spaces or Xs and Os
    for row in range(3):
        for col in range(2):
            if board[row][col] is None:
                board_string = board_string + "   |  "
            else:
                board_string = board_string + board[row][col] + "  |  "
        if board[row][2] is None:
            board_string = board_string + "  "
        else:
            board_string = board_string + board[row][2] + "  "
        board_string = board_string + "\n     |     |     \n  "
        # only want lines in the middle
        if row != 2:
            board_string = board_string + "--------------"
            board_string = board_string + "\n     |     |     \n  "

    print(board_string)


def convert_move(move, board, player):
    """
    Takes a move as a string and places the move on the
    board for the correct player. Returns a boolean representing
    whether it was a valid move.

    :param move: a string representing the move
    :param board: the game board
    :param player: the player who made the move
    :return: a boolean representing whether the move was valid - modifies
    the game board as well
    """

    # capitalize the string so that a variety of capitalizations are accepted
    cap_move = move.upper()

    # split the string into row and col
    row_str = cap_move.split()[0]
    col_str = cap_move.split()[1]

    # convert the row string into an integer value
    if row_str == "TOP":
        row = 0
    elif row_str == "MID":
        row = 1
    elif row_str == "BOT":
        row = 2
    else:
        return False

    # convert the col string into an integer value
    if col_str == "LEFT":
        col = 0
    elif col_str == "MIDDLE":
        col = 1
    elif col_str == "RIGHT":
        col = 2
    else:
        return False

    # having converted, now place the move
    return place_move(board, row, col, player)


def place_move(board, row, col, player):
    """
    Checks to see if a desired square is unoccupied, and
    places a piece there for the proper player if so.

    :param board: a game board
    :param row: the desired row
    :param col: the desired column
    :param player: the desired player
    :return: a boolean representing whether it was successful - modifies
    the input board
    """

    # Determine if an eligible move
    if board[row][col] is None and player == 1:
        board[row][col] = "X"
        return True
    elif board[row][col] is None and player == 2:
        board[row][col] = "O"
        return True
    else:
        return False


def compute_move(board):
    """
    Chooses a valid move for the computer to make
    and plays it.

    :param board: the game board
    :return: nothing - modifies the game board
    """

    # check to see if you can win by playing somewhere
    for row in range(3):
        for col in range(3):
            temp_board = copy.deepcopy(board)
            if place_move(temp_board, row, col, 2):
                # the only person that can win from us playing is us
                if check_win(temp_board):
                    # win game
                    place_move(board, row, col, 2)
                    return

    # check to see if we block by playing somewhere
    for row in range(3):
        for col in range(3):
            temp_board = copy.deepcopy(board)
            if place_move(temp_board, row, col, 1):
                # check if they win from playing here
                if check_win(temp_board):
                    # block if so
                    place_move(board, row, col, 2)
                    return

    # if we don't stop them, or win ourselves, just play random
    while True:
        row = random.randrange(3)
        col = random.randrange(3)
        if place_move(board, row, col, 2):
            return


def check_win(board):
    """
    Reads the game board to determine if a player has won.
    :param board: the game board
    :return: the letter of the winning player or None if there is not one
    """

    # check horizontals
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][0] == board[row][2] and board[row][0] is not None:
            return board[row][0]

    # check verticals
    for col in range(3):
        if board[0][col] == board[1][col] and board[0][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # check diagonals
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


# introduce the game to the player(s)
print("How to play: Choose a square by typing first the vertical location (\"top,\" \"mid,\" \"bot\")\n"
      "and then the horizontal location (\"right,\" \"middle,\" \"left\").\n")

# determine desired number of players
num_players = input("Enter \'1\' for 1 player or \'2\' for 2 players: ")

# set game variables
game_over = False
turn = 1
board = [[None, None, None], [None, None, None],
         [None, None, None]]

print_board(board)

# actual game function
if int(num_players) == 2:
    # run until a player wins
    while not game_over:
        # force them to make valid moves
        valid_turn = False
        while not valid_turn:
            # determine whose move
            if turn % 2 == 1:
                move = input("Player one make a move: ")
                if convert_move(move, board, 1):
                    valid_turn = True
                else:
                    print("Invalid Move! Try Again!")
            else:
                move = input("Player two make a move: ")
                if convert_move(move, board, 2):
                    valid_turn = True
                else:
                    print("Invalid Move! Try Again!")

        print_board(board)
        turn += 1
        if check_win(board) is not None:
            game_over = True
            if check_win(board) == "X":
                winner = "one"
            else:
                winner = "two"
            print("Player " + winner + " is the winner!")

elif int(num_players) == 1:
    # run until a player wins
    while not game_over:
        valid_turn = False
        while not valid_turn:
            if turn % 2 == 1:
                move = input("Player one make a move: ")
                if convert_move(move, board, 1):
                    valid_turn = True
                else:
                    print("Invalid Move! Try Again!")
            else:
                print("Computer Moving")
                wait(500)
                compute_move(board)
                valid_turn = True

        print_board(board)
        turn += 1
        if check_win(board) is not None:
            game_over = True
            if check_win(board) == "X":
                winner = "one"
            else:
                winner = "two"
            print("Player " + winner + " is the winner!")


else:
    print("Invalid number of players.")
    quit()
