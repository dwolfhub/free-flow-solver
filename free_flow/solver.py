from . import objects


def get_adjacent_cells(cell):
    """Given a cell, returns 4 tuples in a tuple representing 
    the x and y values of the four adjacent cells.

    May return negative indexes, which should be ignored.
    Starts to the right and moves clock-wise
    """
    return (
        (cell.x + 1, cell.y), 
        (cell.x, cell.y + 1), 
        (cell.x - 1, cell.y),
        (cell.x, cell.y - 1),
    )

class PipeSolver(object):
    def __init__(self, puzzle, pipe):
        self.puzzle = puzzle
        self.pipe = pipe


    def get_current_cell(self):
        # get the current cell of the pipe
        cell = self.pipe.start
        if len(self.pipe.steps):
            cell = self.pipe.steps[-1]

        return cell;
       
        
    def get_possible_next_moves(self):
        # if pipe complete, no possible moves
        if self.pipe.complete:
            return ()

        current_cell = self.get_current_cell()
        adj_cells = get_adjacent_cells(self.get_current_cell())

        # list of possible moves
        moves = []
        
        # check for openings and add them to the list
        for adj_cell in adj_cells:
            try:
                if not self.puzzle.cells[adj_cell[0]][adj_cell[1]] or (
                    # remember that the end is an opening
                    self.pipe.stop.x == adj_cell[0] and self.pipe.stop.y == adj_cell[1]
                ):
                    moves.append(objects.Cell(adj_cell[0], adj_cell[1]))
            except KeyError:
                pass
            
        return moves

    def take_only_available_steps(self):
        poss_moves = self.get_possible_next_moves()

        if len(poss_moves) == 1:
            move = poss_moves[0]
            # is our own possible move to complete the pipe?
            if move.x == self.pipe.stop.x and move.y == self.pipe.stop.y:
                self.pipe.complete = True
                return

            self.pipe.steps.append(move)
            self.take_only_available_steps()


def take_only_available_steps(puzzle):
    pipes = []
    for pipe in puzzle.pipes:
        pipes.append(take_only_available_step(puzzle, pipe))
    
    puzzle.pipes = pipes

    return puzzle


def solve(puzzle):
    puzzle = take_only_available_steps(puzzle)


