
class Pipe(object):
    def __init__(self, start, stop):
        """Creates a pipe

        Accepts Cells start and stop
        """
        self._start = start
        self._stop = stop


class Cell(object):
    def __init__(self, x, y):
        """Create a Cell

        Accepts integers x and y
        """
        self._x = x
        self._y = y


