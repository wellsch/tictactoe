# define functions
def print_board(board):
    """
      Creates a string representation of the playing board.
      Inputs:
            - board: a list of lists of length three containing the elements
            "X," "O," or None
      Returns: None
      Prints: the board
      """
    # declare the board string
    board_string = "     |     |     \n  "

    # print the empty spaces or Xs and Os
    for row in range(3):
        for col in range(2):
            if board[row][col] == (None, None):
                board_string = board_string + "   |  "
            else:
                board_string = board_string + board[row][col][0] + "  |  "
        if board[row][2] == (None, None):
            board_string = board_string + "  "
        else:
            board_string = board_string + board[row][2][0] + "  "
        board_string = board_string + "\n     |     |     \n  "
        # only want lines in the middle
        if row != 2:
            board_string = board_string + "--------------"
            board_string = board_string + "\n     |     |     \n  "

    print(board_string)


def convert_move(move, board, player):
    """
      Takes in a move as a string and then places the move in the board
      for the correct player. Returns a boolean representing whether it
      was a valid move.
      Inputs:
            - move: the move as a string
            - board: the 2D array representing the board
            - player: the player who made the move
      Returns: a boolean representing whether it was a valid move
      Modifies: the board
      """
    # capitalize the string so that a variety of capitalizations are accepted
    cap_move = move.upper()

    # split the string into row and col
    row_str = cap_move.split()[0]
    row = None
    col_str = cap_move.split()[1]
    col = None

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

    # Determine if an eligible move
    if board[row][col] == (None, None) and player == 1:
        board[row][col] = ("X", player)
        return True
    elif board[row][col] == (None, None) and player == 2:
        board[row][col] = ("O", player)
        return True
    else:
        return False


def check_win(board):
    """
      Reads a board to determine if a player has won the game
      Inputs:
            - board: a 2D array representing the board
      Returns: an integer corresponding to a winning player or None
      if there is not one
      """
    # check horizontals
    for row in range(3):
        if board[row][0][0] == board[row][1][0] and board[row][0][0] == board[row][2][0]:
            return board[row][0][0]

    # check verticals
    for col in range(3):
        if board[0][col][0] == board[1][col][0] and board[0][col][0] == board[2][col][0]:
            return board[0][col][0]

    # check diagonals
    if board[0][0][0] == board[1][1][0] and board[0][0][0] == board[2][2][0] and board[0][0][0] != None:
        return board[0][0][0]
    if board[0][2][0] == board[1][1][0] and board[0][2][0] == board[2][0][0] and board[0][2][0] != None:
        return board[0][2][0]

    return None


# introduce the game to the player(s)
print("How to play: Choose a square by typing first the vertical location (\"top,\" \"mid,\" \"bot\")\n"
      "and then the horizontal location (\"right,\" \"middle,\" \"left\").\n")

# determine desired number of players
num_players = input("Enter \'1\' for 1 player or \'2\' for 2 players: ")

# set global variables
game_over = False
turn = 1
board = [[(None, None), (None, None), (None, None)], [(None, None), (None, None), (None, None)],
         [(None, None), (None, None), (None, None)]]
print_board(board)

if int(num_players) == 2:
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
                move = input("Player two make a move: ")
                if convert_move(move, board, 2):
                    valid_turn = True
                else:
                    print("Invalid Move! Try Again!")

        print_board(board)
        turn += 1
        if check_win(board) is not None:
            game_over = True
            print("Player " + check_win(board) + " is the winner!")
