import tkinter as tk
from tkinter import messagebox
from queue import PriorityQueue
 
def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

# Function to check if a number can be placed in a cell
def is_valid(grid, num, row, col):
    for i in range(9):
        if grid[row][i] == num:
            return False
        if grid[i][col] == num:
            return False
        if grid[(row//3)*3 + i//3][(col//3)*3 + i%3] == num:
            return False
    return True

def get_f_score(grid):
    f_score = 0
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                f_score += 1
    return f_score

def solve_sudoku(grid):
    # using a priority queue and heuristic function to solve the Sudoku puzzle
    pq = PriorityQueue()
    pq.put((0, grid))
    while not pq.empty():
        _, curr_grid = pq.get()
        empty_cell = find_empty(curr_grid)
        if empty_cell is None:
            return curr_grid
        row, col = empty_cell
        for num in range(1, 10):
            if is_valid(curr_grid, num, row, col):
                new_grid = [row[:] for row in curr_grid]
                new_grid[row][col] = num
                f = get_f_score(new_grid)
                pq.put((f, new_grid))

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

        # Solve the Sudoku puzzle using the A* algorithm
        solved_grid = solve_sudoku(self.grid)

        # Update the entry widgets with the solved Sudoku grid
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(solved_grid[i][j]))


    
    def solveBoard(self):
        # Solve the board
        if solve(self.board):
            # Display the solved board
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(self.board[i][j]))
        else:
            messagebox.showerror("Unsolvable", "The puzzle cannot be solved.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(master=root)
    app.mainloop()