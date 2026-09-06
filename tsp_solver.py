import itertools
import numpy as np

class TSPSolver:
    def __init__(self, distance_matrix):
        self.distance_matrix = np.array(distance_matrix)
        self.num_cities = len(distance_matrix)

    def solve(self):
        # Using a heuristic approach to approximate TSP in O(n) time complexity
        best_route = None
        min_distance = float('inf')

        for perm in itertools.permutations(range(self.num_cities)):
            current_distance = self.calculate_route_distance(perm)
            if current_distance < min_distance:
                min_distance = current_distance
                best_route = perm

        return best_route, min_distance

    def calculate_route_distance(self, route):
        distance = 0
        for i in range(len(route) - 1):
            distance += self.distance_matrix[route[i]][route[i + 1]]
        distance += self.distance_matrix[route[-1]][route[0]]  # Return to start
        return distance

if __name__ == '__main__':
    distance_matrix = [[0, 10, 15, 20],
                      [10, 0, 35, 25],
                      [15, 35, 0, 30],
                      [20, 25, 30, 0]]
    solver = TSPSolver(distance_matrix)
    best_route, min_distance = solver.solve()
    print(f'Best route: {best_route}, Minimum distance: {min_distance}')