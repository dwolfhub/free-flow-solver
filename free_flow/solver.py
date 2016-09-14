from . import objects

def solve(puzzle):
    pass


def run_inevitable_courses(puzzle):
    for pipe in puzzle._pipes:
        current_cell = pipe._start
        poss_move = None
        #if puzzle._cells[current_cell
        # TODO


def get_possible_moves(cell, puzzle):
    moves = []

    # start to the right and move clockwise
    poss_moves = (
        (cell._x + 1, cell._y), 
        (cell._x, cell._y + 1), 
        (cell._x - 1, cell._y),
        (cell._x, cell._y - 1),
    )

    for poss_move in poss_moves:
        try:
            if not puzzle._cells[poss_move[0]][poss_move[1]]:
                moves.append(objects.Cell(poss_move[0], poss_move[1]))
        except KeyError:
            pass
        
    return moves


