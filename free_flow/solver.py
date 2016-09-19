from . import objects


def get_possible_moves(pipe, puzzle):
    if pipe._complete:
        return ()
    
    # get the current cell of the pipe
    cell = pipe._start
    if len(pipe._steps):
        cell = pipe._steps[-1]

    moves = []

    # start to the right and move clockwise
    poss_moves = (
        (cell._x + 1, cell._y), 
        (cell._x, cell._y + 1), 
        (cell._x - 1, cell._y),
        (cell._x, cell._y - 1),
    )

    # check for openings and add them to the list
    for poss_move in poss_moves:
        try:
            # remember that the end is an opening
            if (pipe._stop._x == poss_move[0] and pipe._stop._y == poss_move[1]) or not puzzle._cells[poss_move[0]][poss_move[1]]:
                moves.append(objects.Cell(poss_move[0], poss_move[1]))
        except KeyError:
            pass
        
    return moves


def take_only_available_step(puzzle, pipe):
    poss_moves = get_possible_moves(pipe, puzzle)

    if len(poss_moves) == 1:
        pipe._steps.append(poss_moves[0])

        return take_only_available_step(puzzle, pipe)
    else:
        return pipe 


def take_only_available_steps(puzzle):
    # TODO do this from end to start as well 
    pipes = []
    for pipe in puzzle._pipes:
        pipes.append(take_only_available_step(puzzle, pipe))
    
    puzzle._pipes = pipes

    return puzzle


def solve(puzzle):
    puzzle = take_only_available_steps(puzzle)


