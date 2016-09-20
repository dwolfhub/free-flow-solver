from free_flow import objects, input_parser, solver
import unittest

"""
Objects
"""

class PipeTest(unittest.TestCase):
    def test_start_and_stop_set(self):
        start = objects.Cell(1, 1)
        stop = objects.Cell(2, 2)
        pipe = objects.Pipe(start, stop)
        
        self.assertEqual(1, pipe.start.x)
        self.assertEqual(1, pipe.start.y)
        self.assertEqual(2, pipe.stop.x)
        self.assertEqual(2, pipe.stop.y)
        

class CellTest(unittest.TestCase):
    def test_x_and_y_set(self):
        cell = objects.Cell(1, 2)
        
        self.assertEqual(1, cell.x)
        self.assertEqual(2, cell.y)

class PuzzleTest(unittest.TestCase):
    def test_sizes_and_pipes_set(self):
        puzzle = objects.Puzzle(2, 2, [
            objects.Pipe(
                objects.Cell(0, 0),
                objects.Cell(1, 1)
            )
        ])

        self.assertEqual(2, puzzle.size_x)
        self.assertEqual(2, puzzle.size_y)
        self.assertEqual(0, puzzle.pipes[0].start.x)


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

        self.assertEqual(5, puzzle.size_x)
        self.assertEqual(5, puzzle.size_y)
        self.assertEqual(5, len(puzzle.pipes))
        self.assertEqual(1, puzzle.pipes[0].start.x)
        self.assertEqual(0, puzzle.pipes[0].start.y)

"""
Solver
"""

class GetAdjacentCellsTest(unittest.TestCase):
    def test_returns_adjacent_cells(self):
        cell = objects.Cell(0, 0)
        adj_cells = solver.get_adjacent_cells(cell)

        self.assertEqual(1, adj_cells[0][0])
        self.assertEqual(0, adj_cells[0][1])
        self.assertEqual(0, adj_cells[1][0])
        self.assertEqual(1, adj_cells[1][1])
        self.assertEqual(-1, adj_cells[2][0])
        self.assertEqual(0, adj_cells[2][1])
        self.assertEqual(0, adj_cells[3][0])
        self.assertEqual(-1, adj_cells[3][1])


class GetCurrentCellTest(unittest.TestCase):
    def test_uses_start_cell(self):
        pipe = objects.Pipe(
            objects.Cell(0, 0),
            objects.Cell(1, 1)
        )
        puzzle = objects.Puzzle(3, 3, [pipe])
        ps = solver.PipeSolver(puzzle, pipe)
        cell = ps.get_current_cell()
        
        self.assertEqual(0, cell.x)
        self.assertEqual(0, cell.y)

    def test_uses_last_step(self):
        pipe = objects.Pipe(
            objects.Cell(0, 0),
            objects.Cell(1, 1)
        )
        pipe.steps.append(
            objects.Cell(0, 1)
        )
        puzzle = objects.Puzzle(3, 3, [pipe])
        ps = solver.PipeSolver(puzzle, pipe)
        cell = ps.get_current_cell()
        
        self.assertEqual(0, cell.x)
        self.assertEqual(1, cell.y)


class GetPossibleMovesTest(unittest.TestCase):
    def test_one_possible_move_in_the_corner(self):
        pipe = objects.Pipe(
            objects.Cell(0, 0),
            objects.Cell(1, 1)
        )
        puzzle = objects.Puzzle(3, 3, [pipe])
        puzzle.cells[0][1] = True
        ps = solver.PipeSolver(puzzle, pipe)
        moves = ps.get_possible_next_moves()

        self.assertEqual(1, len(moves))
        self.assertEqual(1, moves[0].x)
        self.assertEqual(0, moves[0].y)
 
    def test_two_possible_moves_in_the_corner(self):
        pipe = objects.Pipe(
            objects.Cell(0, 0),
            objects.Cell(1, 1)
        )
        puzzle = objects.Puzzle(3, 3, [pipe])
        ps = solver.PipeSolver(puzzle, pipe)
        moves = ps.get_possible_next_moves()

        self.assertEqual(2, len(moves))
        self.assertEqual(1, moves[0].x)
        self.assertEqual(0, moves[0].y)
        self.assertEqual(0, moves[1].x)
        self.assertEqual(1, moves[1].y)

    def test_three_possible_moves_on_a_side(self):
        pipe = objects.Pipe(
            objects.Cell(0, 1),
            objects.Cell(2, 2)
        )
        puzzle = objects.Puzzle(3, 3, [pipe])
        ps = solver.PipeSolver(puzzle, pipe)
        moves = ps.get_possible_next_moves()

        self.assertEqual(3, len(moves))
        self.assertEqual(1, moves[0].x)
        self.assertEqual(1, moves[0].y)
        self.assertEqual(0, moves[1].x)
        self.assertEqual(2, moves[1].y)
        self.assertEqual(0, moves[2].x)
        self.assertEqual(0, moves[2].y)

    def test_four_possible_moves(self):
        pipe = objects.Pipe(
            objects.Cell(1, 1),
            objects.Cell(3, 3)
        )
        puzzle = objects.Puzzle(4, 4, [pipe])
        ps = solver.PipeSolver(puzzle, pipe)
        moves = ps.get_possible_next_moves()

        self.assertEqual(4, len(moves))
        self.assertEqual(2, moves[0].x)
        self.assertEqual(1, moves[0].y)
        self.assertEqual(1, moves[1].x)
        self.assertEqual(2, moves[1].y)
        self.assertEqual(0, moves[2].x)
        self.assertEqual(1, moves[2].y)
        self.assertEqual(1, moves[3].x)
        self.assertEqual(0, moves[3].y)


class TestTakeOnlyAvailableStep(unittest.TestCase):
    def test_two_steps_available(self):
        # should return the same pipe since there isn't just one optional step
        pipe = objects.Pipe(
            objects.Cell(0, 0),
            objects.Cell(1, 1)
        )
        puzzle = objects.Puzzle(3, 3, [pipe])
        ps = solver.PipeSolver(puzzle, pipe)
        ps.take_only_available_steps()

        self.assertEqual(pipe, ps.pipe)

    def test_one_step_avaiable(self):
        pipe = objects.Pipe(
            objects.Cell(0, 0),
            objects.Cell(1, 1)
        )
        puzzle = objects.Puzzle(3, 3, [pipe])
        puzzle.cells[0][1] = True
        ps = solver.PipeSolver(puzzle, pipe)
        ps.take_only_available_steps()

        self.assertEqual(1, len(ps.pipe.steps))



if __name__ == '__main__':
    unittest.main()
