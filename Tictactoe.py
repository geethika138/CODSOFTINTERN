import math

PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]               
    ]
    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False

def get_empty_positions(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]

def minimax(board, depth, is_maximizing):
    if check_winner(board, PLAYER_X):
        return 10 - depth
    if check_winner(board, PLAYER_O):
        return depth - 10
    if not get_empty_positions(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for position in get_empty_positions(board):
            board[position] = PLAYER_X
            score = minimax(board, depth + 1, False)
            board[position] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for position in get_empty_positions(board):
            board[position] = PLAYER_O
            score = minimax(board, depth + 1, True)
            board[position] = EMPTY
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for position in get_empty_positions(board):
        board[position] = PLAYER_X
        score = minimax(board, 0, False)
        board[position] = EMPTY
        if score > best_score:
            best_score = score
            move = position
    return move

def play_game():
    board = [EMPTY] * 9
    first_player = input("Do you want to go first? (y/n): ").strip().lower()

    if first_player == 'y':
        current_player = PLAYER_O  
    else:
        current_player = PLAYER_X  

    print("Welcome to Tic-Tac-Toe Game!")
    print_board(board)

    while True:
        if current_player == PLAYER_X:
            print("AI(X player) is thinking...")
            move = best_move(board)
            if move is not None:
                board[move] = PLAYER_X
            print("AI(X player) made a move.")
        else:
            move = None
            while move is None or board[move] != EMPTY:
                try:
                    move = int(input("Your move as O: "))
                    if move not in get_empty_positions(board):
                        print("Invalid move. Try again.")
                        move = None
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 8.")
                    continue
            board[move] = PLAYER_O

        print_board(board)

        if check_winner(board, PLAYER_X):
            print("AI(X player) wins!")
            break
        elif check_winner(board, PLAYER_O):
            print("You(O player) win!")
            break
        elif not get_empty_positions(board):
            print("It's a tie.....hurrah!")
            break

        current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

if __name__ == "__main__":
    play_game()
