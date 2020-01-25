import unittest
import main

board = [
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
        self.assertFalse(main.is_used_col(board_col_ok, 0, 2))
        self.assertTrue(main.is_used_col(board_col_no, 0, 2))

    def test_is_used_row(self):
        self.assertFalse(main.is_used_row(board_row_ok, 0, 2))
        self.assertTrue(main.is_used_row(board_row_no, 0, 2))

    def test_is_used_box(self):
        self.assertFalse(main.is_used_box(board_box, 0, 2))
        self.assertTrue(main.is_used_box(board_box, 1, 0))
        self.assertFalse(main.is_used_box(board_box, 1, 2))

    def test_is_safe(self):
        self.assertFalse(main.is_safe(board_box, 0, 1))
        self.assertTrue(main.is_safe(board_safe, 1, 5))
        self.assertTrue(main.is_safe(board_safe, 2, 4))
        self.assertTrue(main.is_safe(board_safe, 3, 4))
        self.assertFalse(main.is_safe(board_not_safe_col, 0, 1))
        self.assertFalse(main.is_safe(board_not_safe_row, 0, 1))


