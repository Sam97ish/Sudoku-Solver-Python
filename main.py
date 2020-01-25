
def print_board(bo):
    '''

    :param bo: takes in a Sudoku board.
    :return: prints out the board on console.
    '''
    for row in range(len(bo)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - - ")

        for col in range(len(bo[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")  # the end is for continuing on the same line

            if col == 8:
                print(bo[row][col])
            else:
                print(str(bo[row][col]) + " ", end="")


def get_empty_location(bo, list):
    '''

        :param bo: takes in the Sudoku board as argument.
        :return: the first empty location found.
    '''

    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == 0 and not(list[0] == row and list[1] == col):
                list[0] = row
                list[1] = col
                return True
    return False


def full_board(bo):
    ''' :return boolean if  board is full '''
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == 0:
                return False
    return True


def is_used_col(bo, row, col):
    ''' :return boolean if the number is used in it's col (returns true if the number is already used) '''
    already_used = False
    possible_row = 0
    while possible_row < len(bo) and not already_used:
        if possible_row != row:  # to prevent it from checking the number given.
            already_used = bo[row][col] == bo[possible_row][col]
        possible_row += 1

    return already_used


def is_used_row(bo, row, col):
    ''' :return boolean if the number is used in it's row (returns true if the number is already used) '''
    already_used = False
    possible_col = 0
    while possible_col < len(bo[0]) and not already_used:
        if possible_col != col:  # to prevent it from checking the number given.
            already_used = bo[row][col] == bo[row][possible_col]
        possible_col += 1

    return already_used


def is_used_box(bo, row, col):
    ''' :return boolean if the number is used in it's 3x3 box (returns true if already used) '''
    start_row = row
    start_col = col
    already_used = False

    if row % 2 != 0 and row != 0:
        start_row -= 1  # if number is on an even row, the rest of it's box is the row above it.

    # the start col of every box is a multi of 3, the following 2 tests will place start_col at the correct start.
    # we will execute this code only if the number is on the second or third square of a box.
    if (col-1) % 3 == 0:
        start_col -= 1
    elif (col-2) % 3 == 0:
        start_col -= 2

    # possible_row and possible_col should now be at the starting point of the box
    possible_col = start_col
    possible_row = start_row
    while possible_row <= start_row+1 and not already_used:

        if possible_col == start_col+3:
            possible_col = start_col
            possible_row += 1
            continue  # so that col is not incremented in this loop
        elif not(row == possible_row and col == possible_col):  # to prevent it from checking the number given.
            already_used = bo[row][col] == bo[possible_row][possible_col]
        possible_col += 1
    return already_used


def is_safe(bo, row, col):
    ''' :returns boolean if a number is safe to consider for a location '''
    return not(is_used_col(bo, row, col) or is_used_row(bo, row, col) or is_used_box(bo, row, col))


# backtracking function
def solve_sudoku(bo):

    last_seen_location = [-1, -1]  # row, col

    if full_board(bo):
        return True
    else :
        get_empty_location(bo, last_seen_location)

    row = last_seen_location[0]
    col = last_seen_location[1]
    for num in range(1, 10):

        bo[row][col] = num

        if is_safe(bo, row, col):
            print(row, col)
            if solve_sudoku(bo):

                return True

        bo[row][col] = 0

    return False


if __name__ == "__main__":
    # sudoku (L5: #683189815)
    Board = [
        [0, 0, 5, 0, 0, 0, 9, 0, 0],
        [4, 0, 0, 0, 6, 0, 0, 0, 2],
        [0, 7, 0, 4, 3, 0, 0, 0, 8],
        [0, 0, 6, 0, 9, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 5, 1, 0, 0],
        [8, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 3, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 7, 8, 0]
    ]

    board = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0], # 0 even
        [5, 2, 0, 0, 0, 0, 0, 0, 0], # 1 odd must go up
        [0, 8, 7, 0, 0, 0, 0, 3, 1], # 2 even
        [0, 0, 3, 0, 1, 0, 0, 8, 0], # 3 odd
        [9, 0, 0, 8, 6, 3, 0, 0, 5], # 4 even
        [0, 5, 0, 0, 9, 0, 6, 0, 0], # 5 odd
        [1, 3, 0, 0, 0, 0, 2, 5, 0], # 6 even
        [0, 0, 0, 0, 0, 0, 0, 7, 4], # 7 odd
        [0, 0, 5, 2, 0, 6, 3, 0, 0]  # 8 even
    ]

    if solve_sudoku(board):
        print_board(board)
    else:
        print("There's no solution")
