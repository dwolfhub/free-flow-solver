
class Pipe(object):
    def __init__(self, start, stop):
        """Creates a pipe

        Accepts Cells start and stop
        """
        self.start = start
        self.stop = stop
        self.steps = []
        self.complete = False


class Cell(object):
    def __init__(self, x, y):
        """Create a Cell

        Accepts integers x and y
        """
        self.x = x
        self.y = y


class Puzzle(object):
    def __init__(self, sizex, sizey, pipes):
        """Create a puzzle

        Accepts int size and list of Pipes pipes
        Creates map (self.cells) of the puzzle in its current state for reference
        """
        cells = {} 
        for i in xrange(0, sizex):
            cells[i] = {} 
            for j in xrange(0, sizey):
                cells[i][j] = None

        for i in pipes:
            cells[i.start.x][i.start.y] = True
            cells[i.stop.x][i.stop.y] = True
        
        self.cells = cells
        self.size_x = sizex
        self.size_y = sizey
        self.pipes = pipes
