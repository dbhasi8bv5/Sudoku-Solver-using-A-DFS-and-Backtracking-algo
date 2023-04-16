import tkinter as tk


def solve_sudoku(board):
    if not find_empty(board):
        return True
    else:
        row, col = find_empty(board)

    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def valid(board, num, pos):
    # Check row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


class SudokuGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid = [[0 for i in range(9)] for j in range(9)]
        self.create_widgets()

    def create_widgets(self):
        # Create the 9x9 grid of entry widgets for the Sudoku board
        self.entries = [[None for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                self.entries[i][j] = tk.Entry(self.master, width=2, font=("Helvetica", 20))
                self.entries[i][j].grid(row=i, column=j)

        # Create the Solve button to solve the Sudoku puzzle
        self.solve_button = tk.Button(self.master, text="Solve", command=self.solve)
        self.solve_button.grid(row=9, column=4)

    def solve(self):
        # Get the values from the entry widgets and create a Sudoku grid
        for i in range(9):
            for j in range(9):
                try:
                    self.grid[i][j] = int(self.entries[i][j].get())
                except ValueError:
                    self.grid[i][j] = 0

        # Solve the Sudoku puzzle using the backtracking algorithm
        if solve_sudoku(self.grid):
            # Update the entry widgets with the solved Sudoku grid
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(self.grid[i][j]))
        else:
            print("Invalid Sudoku board")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(master=root)
    app.mainloop()
