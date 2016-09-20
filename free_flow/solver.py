from . import objects


def get_adjacent_cells(cell):
    # start to the right and move clockwise
    return (
        (cell._x + 1, cell._y), 
        (cell._x, cell._y + 1), 
        (cell._x - 1, cell._y),
        (cell._x, cell._y - 1),
    )

class PipeSolver(object):
    def __init__(self, puzzle, pipe):
        self._puzzle = puzzle
        self._pipe = pipe


    def get_current_cell(self):
        # get the current cell of the pipe
        cell = self._pipe._start
        if len(self._pipe._steps):
            cell = self._pipe._steps[-1]

        return cell;
       
        
    def get_possible_next_moves(self):
        # if pipe complete, no possible moves
        if self._pipe._complete:
            return ()

        current_cell = 
        adj_cells = get_adjacent_cells(self.get_current_cell())

        # list of possible moves
        moves = []
        
        # check for openings and add them to the list
        for adj_cell in adj_cells:
            try:
                if not self._puzzle._cells[adj_cell[0]][adj_cell[1]] or (
                    # remember that the end is an opening
                    self._pipe._stop._x == adj_cell[0] and self._pipe._stop._y == adj_cell[1]
                ):
                    moves.append(objects.Cell(adj_cell[0], adj_cell[1]))
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


