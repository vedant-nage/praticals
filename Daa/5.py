# Design n-Queens matrix having first Queen placed. Use backtracking to place remaining 
# Queens to generate the final n-queen’s matrix. 
# 32CO132


def is_safe(board, row, col, n):
    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_n_queens(board, row + 1, n):
                return True

            # Backtrack
            board[row][col] = 0

    return False


n = int(input("Enter the value of N: "))

board = [[0] * n for _ in range(n)]

# Place the first queen in the first column
board[0][0] = 1

if solve_n_queens(board, 1, n):
    print("\nFinal N-Queens Matrix:")
    for row in board:
        print(row)
else:
    print("No solution exists.")