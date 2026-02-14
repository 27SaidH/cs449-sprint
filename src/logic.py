# src/logic.py

def add(a: int, b: int) -> int:
    return a + b

def is_valid_jump(start, middle, end, board) -> bool:
    """
    Peg Solitaire style jump validation on a grid.
    Rules (simple version):
    - start has a peg (1)
    - middle has a peg (1)
    - end is empty (0)
    - end is exactly 2 squares away horizontally or vertically or diagonally
    """
    sr, sc = start
    mr, mc = middle
    er, ec = end

    # must be 2 away in row/col/diag
    dr = er - sr
    dc = ec - sc
    if (abs(dr), abs(dc)) not in [(2, 0), (0, 2), (2, 2)]:
        return False

    # middle must be exactly halfway
    if (mr, mc) != (sr + dr // 2, sc + dc // 2):
        return False

    # board checks
    return board[sr][sc] == 1 and board[mr][mc] == 1 and board[er][ec] == 0
