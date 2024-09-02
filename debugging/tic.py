def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return not check_winner(board)


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if 0 <= row < 3 and 0 <= col < 3:
                if board[row][col] == " ":
                    board[row][col] = player
                    if check_winner(board):
                        print_board(board)
                        print("Player " + player + " wins!")
                        break
                    elif check_draw(board):
                        print_board(board)
                        print("It's a draw!")
                        break
                    # Changer de joueur
                    player = "O" if player == "X" else "X"
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Invalid row or column. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

tic_tac_toe()
