# tests/test_logic.py
from src.logic import add, is_valid_jump

def test_add_basic():
    assert add(2, 3) == 5

def test_is_valid_jump_horizontal():
    board = [
        [1, 1, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    # jump from (0,0) over (0,1) into (0,2)
    assert is_valid_jump((0, 0), (0, 1), (0, 2), board) is True

def test_is_valid_jump_invalid_distance():
    board = [
        [1, 1, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    # end is only 1 away -> invalid
    assert is_valid_jump((0, 0), (0, 1), (0, 1), board) is False
