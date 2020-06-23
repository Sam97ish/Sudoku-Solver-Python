
class Board_9(object):
    ''' 9*9 sudoku board '''
    board_list  = [[]]
    unsolved_board  = [[]]
    size = 9
    last_seen_location = [-1, -1]  # row, col
    
    def __init__(self,board_list):
        self.board_list = board_list
        self.unsolved_board = board_list
    
    
    def print_board(self):
        '''
        :param self: takes in a Sudoku board.
        :role : prints out the board on console.
        :return: 
        '''
        for row in range(self.size):
            if row % 3 == 0 and row != 0:
                print("- - - - - - - - - - - - - ")
    
            for col in range(self.size):
                if col % 3 == 0 and col != 0:
                    print(" | ", end="")  # the end is for continuing on the same line
    
                if col == 8:
                    print(self.board_list[row][col])
                else:
                    print(str(self.board_list[row][col]) + " ", end="")


    def get_empty_location(self):
        '''
        :param self: takes in a Sudoku board.
        :param list : takes the last seen location where list[0] = row and list[1] = col.
        :role : searches for an empty cell on the board.
        :return: puts the row and col of an empty cell in list.
        '''
        for row in range(self.size):
            for col in range(self.size):
                if self.board_list[row][col] == 0 and not(self.last_seen_location[0] == row and self.last_seen_location[1] == col):
                    self.last_seen_location[0] = row
                    self.last_seen_location[1] = col
                    return True
        return False
        
        
    def full_board(self):
        '''
        :param self: takes in a Sudoku board.
        :role : determines if the board is full.
        :return: true if board is full.
        '''
        for row in range(self.size):
            for col in range(self.size):
                if self.board_list[row][col] == 0:
                    return False
        return True
    
    
    def is_used_col(self,row,col):
        '''
        :param row,col: numbers.
        :role : determines the number at the index[row][col] is used on the column col.
        :return: true if the number is indeed used on col.
        '''
        already_used = False
        possible_row = 0
        while possible_row < len(self.board_list) and not already_used:
            if possible_row != row:  # to prevent it from checking the number given.
                already_used = self.board_list[row][col] == self.board_list[possible_row][col]
            possible_row += 1
    
        return already_used
    
    
    def is_used_row(self,row,col):
        '''
        :param row,col: numbers.
        :role : determines the number at the index[row][col] is used on the same row.
        :return: true if the number is indeed used on the same row.
        '''
        already_used = False
        possible_col = 0
        while possible_col < len(self.board_list[0]) and not already_used:
            if possible_col != col:  # to prevent it from checking the number given.
                already_used = self.board_list[row][col] == self.board_list[row][possible_col]
            possible_col += 1
    
        return already_used
    
    
    def is_used_box(self,row,col):
        '''
        :param row,col: numbers.
        :role : determines the number at the index[row][col] is used on the corresponding 3*3 box.
        :return: true if the number is indeed used on the 3*3 bpx.
        ''' 
        if(row <= 2): #first piece
        
          if(col <= 2):
            return self.check3box(0,0,row,col);
          elif(col >= 6):
            return self.check3box(0,6,row,col);
          else:
            return self.check3box(0,3,row,col);
          
          
        elif(row >= 6): #final piece
            
           if(col <= 2):
            return self.check3box(6,0,row,col);
           elif(col >= 6):
            return self.check3box(6,6,row,col);
           else:
            return self.check3box(6,3,row,col);
          
        else: #middle piece
        
          if(col <= 2):
            return self.check3box(3,0,row,col);
          elif(col >= 6):
            return self.check3box(3,6,row,col);
          else:
            return self.check3box(3,3,row,col);
        
        
    def check3box(self,strrow,strcol,cand_row,cand_col):
        '''
        :param: takes in the beginning of the 3*3 box, and the number to check for.
        :role: helper function called in is_used_box
        :return: true if the number is used in the box
        '''
        for row in range(0,3):
            for col in range(0,3):
                if( not(strrow+row == cand_row and strcol+col == cand_col) and self.board_list[strrow+row][strcol+col] == self.board_list[cand_row][cand_col]):
                    return True;
        return False;
    
    
    def is_safe(self,row,col):
        '''
        :param row,col: numbers.
        :role: uses the three functions above to check if a number is safe in the given cell.
        :return: true if the number is safe.
        '''
        return not(self.is_used_col(row, col) or self.is_used_row(row, col) or self.is_used_box(row, col))
    
    
    def solve_sudoku(self):
        '''
        :param: the sudoku board.
        :role: uses all the functions above to solve the sudoku using a backtracking method.
        :return: solved sudoku.
        '''
        
        if self.full_board():
            return True
        else :
            self.get_empty_location()

        row = self.last_seen_location[0]
        col = self.last_seen_location[1]
        for num in range(1, 10):
            
            self.board_list[row][col] = num
    
            if self.is_safe(row, col):
                
                if self.solve_sudoku():
    
                    return True
    
            self.board_list[row][col] = 0
        
        return False
