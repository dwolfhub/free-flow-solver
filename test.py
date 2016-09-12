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


"""
Input Parsers
"""

class AbstractInputParserTest(unittest.TestCase):
    def test_sets_pipes(self):
        ip = input_parser.AbstractInputParser()

        self.assertTrue(hasattr(ip, '_pipes'))

class FileInputParserTest(unittest.TestCase):
    def test_set_file_sets_file(self):
        fip = input_parser.FileInputParser()
        f = open('/dev/null')
        fip.set_file(f)
        
        self.assertEqual(f, fip._file)

    def test_parse_returns_none_when_no_file(self):
        fip = input_parser.FileInputParser()
        self.assertEqual(None, fip.parse())

    def test_parse_returns_list_of_pipes(self):
        fip = input_parser.FileInputParser()
        f = open('data/test_input_1.txt')
        fip.set_file(f)

        p = objects.Puzzle(5, [
            objects.Pipe(
                objects.Cell(1, 0),
                objects.Cell(0, 3)
            ),
            objects.Pipe(
                objects.Cell(2, 0),
                objects.Cell(0, 4)
            ),
            objects.Pipe(
                objects.Cell(3, 0),
                objects.Cell(3, 4)
            ),
            objects.Pipe(
                objects.Cell(3, 1),
                objects.Cell(2, 2)
            ),
            objects.Pipe(
                objects.Cell(2, 4),
                objects.Cell(3, 3)
            )
        ])

        self.assertEqual(p, fip.parse())


if __name__ == '__main__':
    unittest.main()
