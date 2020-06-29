# check whether the input is valid
def valid(board, x, y, num):
    # check row
    for k in range(0,9):
        if board[y][k] == num:
            return False

    # check col
    for g in range(0,9):
        if board[g][x] == num:
            return False

    # check box valid
        x_box = x // 3
        y_box = y // 3

    for d in range((y_box * 3), y_box * 3 + 3):
        for h in range((x_box * 3), x_box * 3 +3):
            if board[d][h] == num:
                return False
    return True


# check the empty spaces in the board
def empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return None


# find the solution
def solve(board):
    find = empty(board)
    if not find:
        return True
    else:
        y, x = find

    for i in range(1,10):
        if valid(board, x, y, i):
            board[y][x] = i

            # recursion
            if solve(board):
                return True

            # if solve != True, reset the number in the input
            board[y][x] = 0
    return False


# print board
def print_bo(board):
    for x in board:
        for y in x:
            print(y, end='\t')
        print()


