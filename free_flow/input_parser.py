from . import objects

        
def get_sizes_from_first_line(line):
    """The first line of a file should have 3 numbers separated by spaces:
    5 5 5

    The first is the height of the puzzle and the second is the width of
    the puzzle. This method returns those two in a list.
    """
    dims = line.split()

    return int(dims[0]), int(dims[1])


def parse_file(ifile):
    """Parse a puzzle file and return a Puzzle object

    The first line describes the puzzle and each line thereafter describes
    the points which make up the start and end of each pipe
    for example:
    5 5 2
    (5, 5) (1, 1)
    (1, 2) (2, 2)
    """
    while ifile:
        size_x, size_y = get_sizes_from_first_line(ifile.readline())
        pipes = []
         
        for line in ifile:
            points = ''.join([x for x in line if x not in  ['(', ')', ',']]).split()
            pipes.append(
                objects.Pipe(
                    objects.Cell(int(points[0]), int(points[1])),
                    objects.Cell(int(points[2]), int(points[3]))
                )
            )

        return objects.Puzzle(size_x, size_y, pipes)
