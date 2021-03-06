import Board

if __name__ == "__main__":
    # sudoku (L5: #683189815)
    Board1 = [
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

    board1 = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0], 
        [5, 2, 0, 0, 0, 0, 0, 0, 0], 
        [0, 8, 7, 0, 0, 0, 0, 3, 1], 
        [0, 0, 3, 0, 1, 0, 0, 8, 0], 
        [9, 0, 0, 8, 6, 3, 0, 0, 5], 
        [0, 5, 0, 0, 9, 0, 6, 0, 0], 
        [1, 3, 0, 0, 0, 0, 2, 5, 0], 
        [0, 0, 0, 0, 0, 0, 0, 7, 4], 
        [0, 0, 5, 2, 0, 6, 3, 0, 0]  
    ]
    
    board = [
    [1, 0, 0, 0, 4, 0, 0, 0, 0],
    [0, 9, 2, 6, 0, 0, 3, 0, 0],
    [3, 0, 0, 0, 0, 5, 1, 0, 0],
    [0, 7, 0, 1, 0, 0, 0, 0, 4],
    [0, 0, 4, 0, 5, 0, 6, 0, 0],
    [2, 0, 0, 0, 0, 4, 0, 8, 0],
    [0, 0, 9, 4, 0, 0, 0, 0, 1],
    [0, 0, 8, 0, 0, 6, 5, 2, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 6]
    ]

Newboard = Board.Board_9(board)
if(Newboard.solve_sudoku()):
    Newboard.print_board()
else:
    print("there's no solution")
    
