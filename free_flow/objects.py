
class Pipe(object):
    def __init__(self, start, stop):
        """Creates a pipe

        Accepts Cells start and stop
        """
        self._start = start
        self._stop = stop
        self._steps = []
        self._complete = False


class Cell(object):
    def __init__(self, x, y):
        """Create a Cell

        Accepts integers x and y
        """
        self._x = x
        self._y = y


class Puzzle(object):
    def __init__(self, size_x, size_y, pipes):
        """Create a puzzle

        Accepts int size and list of Pipes pipes
        Creates map (self._cells) of the puzzle in its current state for reference
        """
        cells = {} 
        for i in xrange(0, size_x):
            cells[i] = {} 
        for j in xrange(0, size_y):
            cells[i][j] = None

        for i in pipes:
            cells[i._start._x][i._start._y] = True
            cells[i._stop._x][i._stop._y] = True
        
        self._cells = cells
        self._size_x = size_x
        self._size_y = size_y
        self._pipes = pipes
