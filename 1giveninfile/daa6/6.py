N = 8

board = [[0 for _ in range(N)] for _ in range(N)]


def is_safe(row, col):
    # Check same column in previous rows
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
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_queens(row):
    if row == N:
        return True

    # First queen is already fixed at (0, 0)
    if row == 0:
        board[0][0] = 1
        return solve_queens(row + 1)

    for col in range(N):
        if is_safe(row, col):
            board[row][col] = 1

            if solve_queens(row + 1):
                return True

            # Backtrack if this placement leads to no solution
            board[row][col] = 0

    return False


if solve_queens(0):
    print("Final 8-Queens matrix:")
    for row in board:
        print(row)
else:
    print("No solution found.")