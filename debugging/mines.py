import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.total_cells = width * height
        self.non_mine_cells = self.total_cells - mines

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # Ne pas compter la cellule elle-même
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                # Vérifier les limites du tableau
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count


    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            print("\033[93mInvalid coordinates. Please enter values within the board limits.\033[0m")
            input("Press Enter to continue...")
            return True  # Continue the game
        
        if (y * self.width + x) in self.mines:
            return False
        if not self.revealed[y][x]:
            self.revealed[y][x] = True
            self.non_mine_cells -= 1
            if self.count_mines_nearby(x, y) == 0:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                            self.reveal(nx, ny)
        return True

    def check_win(self):
        return self.non_mine_cells == 0

    def play(self):
        while True:
            self.print_board()
            user_input = input("Enter x coordinate (or 'q' to quit): ")

            if user_input.lower() == 'q':
                print("\033[91mGame exited.\033[0m")
                input("Press Enter to continue...")
                self.print_board(reveal=True)
                break

            try:
                x = int(user_input)
                y_input = input("Enter y coordinate: ")
            
                # Vérifiez si l'entrée pour y est 'q'
                if y_input.lower() == 'q':
                    print("\033[91mGame exited.\033[0m")
                    input("Press Enter to continue...")
                    self.print_board(reveal=True)
                    break
            
                y = int(y_input)

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("\033[91mGame Over! You hit a mine.\033[0m")
                    break
                if self.check_win():
                    self.print_board(reveal=True)
                    print("\033[92mCongratulations! You've revealed all non-mine cells and won the game!\033[0m")
                    break
            except ValueError:
                print("\033[93mInvalid input. Please enter numbers only.\033[0m")
                input("Press Enter to continue...")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
