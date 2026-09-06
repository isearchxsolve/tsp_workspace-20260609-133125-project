import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from tsp_solver import TSPSolver

class TestTSPSolver(unittest.TestCase):
    def test_solver(self):
        distance_matrix = [[0, 10, 15, 20],
                          [10, 0, 35, 25],
                          [15, 35, 0, 30],
                          [20, 25, 30, 0]]
        solver = TSPSolver(distance_matrix)
        best_route, min_distance = solver.solve()
        self.assertEqual(best_route, (0, 1, 3, 2))  # Example expected route
        self.assertEqual(min_distance, 80)  # Example expected distance

if __name__ == '__main__':
    unittest.main()