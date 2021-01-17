import itertools

def line_ok(e):
    if len(set(e)) != 9: return False
    for i in range(len(e)):
        if e[i] not in range(1,10): return False
    return True
    
def checker(grid):
    bad_rows = [False for row in grid if not line_ok(row)]
    grid = list(zip(*grid))
    bad_cols = [False for col in grid if not line_ok(col)]
    squares = []
    for i in range(0,9,3):
        for j in range(0,9,3):
            square = list(itertools.chain.from_iterable(row[j:j+3] for row in grid[i:i+3]))
            squares.append(square)
    bad_squares = [False for sq in squares if not line_ok(sq)]
    return not any([bad_rows, bad_cols, bad_squares])