#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    winner = None

    while winner is None:
        print_board(board)
        
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input! Row and column must be 0, 1, or 2.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            board[row][col] = player
            winner = check_winner(board)
            if winner is None and check_draw(board):
                break
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Invalid input! Please enter a number.")

    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")

tic_tac_toe()
