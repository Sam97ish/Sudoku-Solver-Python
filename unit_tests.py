import unittest
import Board

board1 = [
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

board_col_ok = [
    [0, 0, 5],
    [4, 0, 0],
    [0, 7, 0],
    [0, 0, 6],
    [0, 0, 0],
    [8, 0, 0],
    [0, 9, 0],
    [0, 4, 3],
    [0, 0, 0]
]
board_col_no = [
    [0, 0, 5],
    [4, 0, 0],
    [0, 7, 0],
    [0, 0, 6],
    [0, 0, 5],
    [8, 0, 0],
    [0, 9, 0],
    [0, 4, 3],
    [0, 0, 0]
]

board_row_ok = [
    [0, 0, 5, 0, 0, 0, 9, 0, 0],
]
board_row_no = [
    [0, 0, 5, 0, 0, 0, 9, 5, 0],
]

board_box = [
    [0, 4, 5, 0, 0, 0],
    [4, 0, 3, 0, 0, 9],
    [0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 5, 0]
]

board_safe = [
    [0, 4, 5, 0, 0, 0],
    [0, 0, 3, 0, 0, 9],
    [0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 5, 0]
]

board_not_safe_col = [
    [0, 4, 5, 0, 0, 0],
    [0, 0, 3, 0, 0, 9],
    [0, 4, 0, 0, 8, 0],
    [0, 0, 0, 0, 5, 0]
]

board_not_safe_row = [
    [0, 4, 5, 0, 0, 4],
    [0, 0, 3, 0, 0, 9],
    [0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 5, 0]
]

class TestIsSafeFunctions(unittest.TestCase):

    def test_is_used_col(self):
        testboard_col_ok = Board.Board_9(board_col_ok)
        testboard_col_no = Board.Board_9(board_col_no)
        
        self.assertFalse(testboard_col_ok.is_used_col(0, 2))
        self.assertTrue(testboard_col_no.is_used_col(0, 2))

    def test_is_used_row(self):
        testboard_row_ok = Board.Board_9(board_row_ok)
        testboard_row_no = Board.Board_9(board_row_no)
        
        self.assertFalse(testboard_row_ok.is_used_row(0, 2))
        self.assertTrue(testboard_row_no.is_used_row(0, 2))

    def test_is_used_box(self):
        testboard_box = Board.Board_9(board_box)

        self.assertFalse(testboard_box.is_used_box(0, 2))
        self.assertTrue(testboard_box.is_used_box(1, 0))
        self.assertFalse(testboard_box.is_used_box(1, 2))

    def test_is_safe(self):
        
        testboard_box = Board.Board_9(board_box)
        testboard_safe = Board.Board_9(board_safe)
        testboard_not_safe_col = Board.Board_9(board_not_safe_col)
        testboard_not_safe_row = Board.Board_9(board_not_safe_row)
        
        self.assertFalse(testboard_box.is_safe( 0, 1))
        self.assertTrue(testboard_safe.is_safe( 1, 5))
        self.assertTrue(testboard_safe.is_safe( 2, 4))
        self.assertFalse(testboard_not_safe_col.is_safe(0, 1))
        self.assertFalse(testboard_not_safe_row.is_safe(0, 1))


