#!/usr/bin/python3

def print_board(board):
    print("   0   1   2")
    print(" ┌───┬───┬───┐")
    for i, row in enumerate(board):
        print(f"{i}│ {' │ '.join(row)} │")
        if i < 2:
            print(" ├───┼───┼───┤")
    print(" └───┴───┴───┘")

def check_winner(board):
    # Vérification des lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérification des colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        # Entrée de l'utilisateur avec gestion des erreurs
        try:
            row_input = input(f"Enter row (0, 1, 2, or 'q' to quit) for player {player}: ")
            if row_input.lower() == 'q':
                print("\033[93mGame exited. Thanks for playing!\033[0m")
                break
            
            row = int(row_input)
            
            col_input = input(f"Enter column (0, 1, 2, or 'q' to quit) for player {player}: ")
            if col_input.lower() == 'q':
                print("\033[93mGame exited. Thanks for playing!\033[0m")
                break
            
            col = int(col_input)

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("\033[93mInvalid input! Row and column must be 0, 1, or 2.\033[0m")
                continue

        except ValueError:
            print("\033[93mInvalid input! Please enter a number.\033[0m")
            continue
        
        if board[row][col] == " ":
            board[row][col] = player
            
            if check_winner(board):
                print_board(board)
                print(f"\033[92mPlayer {player} wins!\033[0m")
                break
            
            if is_board_full(board):
                print_board(board)
                print("\033[93mIt's a draw!\033[0m")
                break
            
            # Changement de joueur
            player = "O" if player == "X" else "X"
        else:
            print("\033[93mThat spot is already taken! Try again.\033[0m")

tic_tac_toe()
