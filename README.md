# Travelling Salesman Problem Solver

## Description
This project implements a solver for the Travelling Salesman Problem (TSP) using a heuristic approach to approximate solutions in O(n) time complexity.

## Features
- Solves TSP using a distance matrix
- Outputs the best route and minimum distance

## Prerequisites
- Python 3.7+
- NumPy library

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration
- No specific configuration is required. Modify the `distance_matrix` in `tsp_solver.py` to test with different cities.

## Running the Application
To run the application, execute:
```bash
python tsp_solver.py
```

## Usage Examples
Modify the `distance_matrix` variable in `tsp_solver.py` to include different distances between cities.

## Project Structure
- `tsp_solver.py`: Main solver implementation.
- `requirements.txt`: Required Python packages.
- `test_tsp_solver.py`: Unit tests for the solver.
- `README.md`: Project documentation.

## Testing
To run the tests, execute:
```bash
python test_tsp_solver.py
```

## Troubleshooting
- Ensure you have the correct version of Python installed.
- If you encounter any import errors, check that all dependencies are installed correctly.