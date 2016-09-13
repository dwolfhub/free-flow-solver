from free_flow import objects, input_parser
import unittest

"""
Objects
"""

class PipeTest(unittest.TestCase):
    def test_start_and_stop_set(self):
        start = objects.Cell(1, 1)
        stop = objects.Cell(2, 2)
        pipe = objects.Pipe(start, stop)
        
        self.assertEqual(1, pipe._start._x)
        self.assertEqual(1, pipe._start._y)
        self.assertEqual(2, pipe._stop._x)
        self.assertEqual(2, pipe._stop._y)
        

class CellTest(unittest.TestCase):
    def test_x_and_y_set(self):
        cell = objects.Cell(1, 2)
        
        self.assertEqual(1, cell._x)
        self.assertEqual(2, cell._y)

class PuzzleTest(unittest.TestCase):
    def test_sizes_and_pipes_set(self):
        puzzle = objects.Puzzle(2, 2, [
            objects.Pipe(
                objects.Cell(0, 0),
                objects.Cell(1, 1)
            )
        ])

        self.assertEqual(2, puzzle._size_x)
        self.assertEqual(2, puzzle._size_y)
        self.assertEqual(0, puzzle._pipes[0]._start._x)


"""
Input Parsers
"""

class GetSizesFromFirstLineTest(unittest.TestCase):
    def test_returns_dims(self):
        fline = '5 5 5'
        self.assertEqual((5, 5), input_parser.get_sizes_from_first_line(fline))

        fline = '50 50 50'
        self.assertEqual((50, 50), input_parser.get_sizes_from_first_line(fline))

        fline = '050 30 2'
        self.assertEqual((50, 30), input_parser.get_sizes_from_first_line(fline))


class FileInputParserTest(unittest.TestCase):
    def test_parse_file_returns_none_when_no_file(self):
        self.assertEqual(None, input_parser.parse_file(None))

    def test_parse_file_returns_list_of_pipes_with_start_and_stop(self):
        puzzle = input_parser.parse_file(open('data/test_input_1.txt'))

        self.assertEqual(5, puzzle._size_x)
        self.assertEqual(5, puzzle._size_y)
        self.assertEqual(5, len(puzzle._pipes))
        self.assertEqual(1, puzzle._pipes[0]._start._x)
        self.assertEqual(0, puzzle._pipes[0]._start._y)


if __name__ == '__main__':
    unittest.main()
