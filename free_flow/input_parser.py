from . import objects

class AbstractInputParser(object):
    def __init__(self):
        self._pipes = []

    def parse(self):
        pass

    def get_pipes(self):
        return self._pipes

        
def _get_sizes_from_first_line(line):
    dims = line.split(' ')

    return dims[0], dims[1]

class FileInputParser(AbstractInputParser):
    def set_file(self, file):
        self._file = file

    def parse(self):
        if not hasattr(self, '_file'):
            return

        while self._file:
            size_x, size_y = _get_sizes_from_first_line(self._file)
            pipes = []
             
            for line in self._file[1:]:
                points = ''.join([x for x in line if x not in  ['(', ')', ',']]).split()
                pipes.append(
                    objects.Pipe(
                        objects.Cell(points[0], points[1]),
                        objects.Cell(points[2], points[3])
                    )
                )

            return objects.Puzzle(size_x, size_y, pipes)

        return

        


class StringInputParser(AbstractInputParser):
    def set_input(self, input_str):
        self._input_str = input_str

    def parse(self):
        if not hasattr(self, '_input_str'):
            return
