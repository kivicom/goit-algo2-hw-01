# Homework: Divide and Conquer Algorithms

## Overview

This project implements two algorithms using the divide and conquer strategy as part of a homework assignment on algorithm analysis:

1. **Task 1: Find Minimum and Maximum Elements**

   - Function: `find_min_max`
   - Finds the minimum and maximum elements in an array using a recursive divide and conquer approach.
   - Time complexity: O(n)

2. **Task 2: Find k-th Smallest Element**

   - Function: `quick_select`
   - Finds the k-th smallest element in an unsorted array using the Quick Select algorithm.
   - Average time complexity: O(n)

## Project Structure

- `src/`
  - `__init__.py`: Marks the directory as a Python package.
  - `min_max.py`: Implementation of the `find_min_max` function (Task 1).
  - `quick_select.py`: Implementation of the `quick_select` function (Task 2).
- `tests/`
  - `__init__.py`: Marks the directory as a Python package.
  - `test_min_max.py`: Unit tests for Task 1.
  - `test_quick_select.py`: Unit tests for Task 2.
- `requirements.txt`: List of dependencies (pytest).
- `README.md`: This file, containing project documentation.

## Requirements

- **Python**: 3.8 or higher
- **Dependencies**:

  - No external dependencies required if using `unittest`.
  - Optional: `pytest` for running tests.

    ```
    pip install -r requirements.txt
    ```

## Setup

1. Clone or download the project repository.
2. (Optional) Create and activate a virtual environment:

   ```
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   .venv\Scripts\activate     # On Windows
   ```

3. Install dependencies (if using pytest):

   ```
   pip install -r requirements.txt
   ```

## Running the Code

- **Task 1 (min_max)**:

  ```
  python src/min_max.py
  ```

  Example output:

  ```
  Array: [4, 2, 7, 1, 9, 3], Minimum: 1, Maximum: 9
  Array: [1], Minimum: 1, Maximum: 1
  Array: [5, 5, 5], Minimum: 5, Maximum: 5
  Array: [2, 1], Minimum: 1, Maximum: 2
  ```

- **Task 2 (quick_select)**:

  ```
  python src/quick_select.py
  ```

  Example output:

  ```
  Array: [4, 2, 7, 1, 9, 3], k: 3, k-th smallest: 3
  Array: [1], k: 1, k-th smallest: 1
  Array: [5, 5, 5], k: 2, k-th smallest: 5
  Array: [2, 1], k: 1, k-th smallest: 1
  ```

## Running Tests

Tests are implemented using `unittest` and can also be run with `pytest`.

- **Using unittest**:

  ```
  python -m unittest discover tests
  ```

- **Using pytest** (recommended):

  ```
  PYTHONPATH=. pytest tests/
  ```

  Note: The `PYTHONPATH=.` ensures the `src` module is found. Alternatively, the test files include `sys.path` modifications to handle imports.

  Example output:

  ```
  collected 12 items
  tests/test_min_max.py ..... [ 50%]
  tests/test_quick_select.py ...... [100%]
  ```

## Notes

- The `find_min_max` function uses a recursive divide and conquer approach, splitting the array into two halves until base cases are reached.
- The `quick_select` function implements the Quick Select algorithm, partitioning the array around a pivot and recursively processing only the relevant partition.
- For improved performance in `quick_select`, consider randomizing the pivot selection to avoid worst-case O(n²) scenarios.
- Tests cover normal cases, edge cases (single element, empty array, invalid k), and repeated elements.

## Troubleshooting

- **ModuleNotFoundError**: If you encounter `No module named 'src'`, ensure:
  - The `__init__.py` files exist in `src/` and `tests/`.
  - Use `PYTHONPATH=.` when running pytest, or verify that test files include `sys.path` modifications.
- **Contact**: If issues persist, reach out to the mentor via Slack.
