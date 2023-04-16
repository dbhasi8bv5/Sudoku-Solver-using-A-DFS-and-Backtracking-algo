import tkinter as tk

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

    def solve_sudoku(self, row, col):
        # Define the recursive backtracking algorithm to solve the Sudoku puzzle
        if col == 9:
            row += 1
            col = 0
            if row == 9:
                return True

        if self.grid[row][col] != 0:
            return self.solve_sudoku(row, col+1)

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.grid[row][col] = num
                if self.solve_sudoku(row, col+1):
                    return True
                self.grid[row][col] = 0

        return False

    def is_valid(self, row, col, num):
        # Check if a number can be placed in a certain cell
        for i in range(9):
            if self.grid[row][i] == num:
                return False
            if self.grid[i][col] == num:
                return False
            if self.grid[row//3*3+i//3][col//3*3+i%3] == num:
                return False
        return True

    def solve(self):
        # Get the values from the entry widgets and create a Sudoku grid
        for i in range(9):
            for j in range(9):
                try:
                    self.grid[i][j] = int(self.entries[i][j].get())
                except ValueError:
                    self.grid[i][j] = 0

        # Solve the Sudoku puzzle using the backtracking algorithm
        if self.solve_sudoku(0, 0):
            # Update the entry widgets with the solved Sudoku grid
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(self.grid[i][j]))

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(master=root)
    app.mainloop()
