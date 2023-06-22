import sys

# Constants for players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY_CELL = ' '

# Function to print the tic-tac-toe board
def print_board(board):
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
        print("|")
    print("---------")

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY_CELL:
                return False
    return True

# Minimax algorithm implementation
def minimax(board, depth, maximizing_player):
    scores = {
        PLAYER_X: 1,
        PLAYER_O: -1,
        'draw': 0
    }

    if check_winner(board, PLAYER_X):
        return scores[PLAYER_X]
    elif check_winner(board, PLAYER_O):
        return scores[PLAYER_O]
    elif is_board_full(board):
        return scores['draw']

    if maximizing_player:
        max_score = -sys.maxsize
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY_CELL:
                    board[i][j] = PLAYER_X
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY_CELL
                    max_score = max(score, max_score)
        return max_score
    else:
        min_score = sys.maxsize
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY_CELL:
                    board[i][j] = PLAYER_O
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY_CELL
                    min_score = min(score, min_score)
        return min_score

# Function to find the best move for the computer using minimax
def get_best_move(board):
    best_score = -sys.maxsize
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY_CELL:
                board[i][j] = PLAYER_X
                score = minimax(board, 0, False)
                board[i][j] = EMPTY_CELL

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

# Function to play the tic-tac-toe game
def play_game():
    board = [[EMPTY_CELL] * 3 for _ in range(3)]
    current_player = PLAYER_X

    while True:
        print_board(board)

        if current_player == PLAYER_X:
            # Human player's turn
            while True:
                move = input("Enter the cell number (1-9): ")
                if move.isdigit() and 1 <= int(move) <= 9:
                    row = (int(move) - 1) // 3
                    col = (int(move) - 1) % 3
                    if board[row][col] == EMPTY_CELL:
                        board[row][col] = PLAYER_O
                        break
                    else:
                        print("Invalid move. Try again.")
                else:
                    print("Invalid input. Try again.")
        else:
            # Computer's turn
            print("Computer's turn...")
            best_move = get_best_move(board)
            if best_move is not None:
                board[best_move[0]][best_move[1]] = PLAYER_X

        if check_winner(board, current_player):
            print_board(board)
            print(current_player, "wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

# Start the game
play_game()
