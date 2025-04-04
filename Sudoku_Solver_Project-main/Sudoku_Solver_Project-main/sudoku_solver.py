# sudoku solver using dfs backtracking............

import streamlit as st
import numpy as np

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Backtrack
                return False
    return True

def main():
    st.title("Sudoku Solver with Streamlit")

    st.write("### Enter Sudoku Puzzle (use 0 for empty cells)")
    sudoku_grid = np.zeros((9, 9), dtype=int)
    grid = []
    for i in range(9):
        row = []
        cols = st.columns(9)
        for j in range(9):
            val = cols[j].number_input("", min_value=0, max_value=9, value=0, key=f"{i}{j}")
            row.append(val)
        grid.append(row)

    if st.button("Solve Sudoku"):
        for i in range(9):
            for j in range(9):
                sudoku_grid[i][j] = int(grid[i][j])
        solution = np.copy(sudoku_grid)
        if solve_sudoku(solution):
            st.success("Sudoku Solved Successfully!")
            st.write("### Solved Sudoku")
            for i in range(9):
                cols = st.columns(9)
                for j in range(9):
                    cols[j].text_input("", value=str(solution[i][j]), disabled=True, key=f"sol{i}{j}")
        else:
            st.error("No solution exists for the provided Sudoku.")

if __name__ == "__main__":
    main()
