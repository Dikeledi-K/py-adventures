# Python Assessment Preparation

This repository contains 15 coding challenges to prepare you for the assessment. The main branch is protected, and changes must be submitted via pull requests. GitHub Actions will run unit tests on PR submission.

## Project Structure
- `solutions.py`: Implementation file with TODOs for 15 functions
- `test_solutions.py`: Unit tests for all functions

## Tasks
Implement these functions in `solutions.py`:
1. `mastermind`: Calculate Mastermind guess results
2. `to_roman`: Convert integer to Roman numeral
3. `binary_search`: Implement binary search
4. `fibonacci`: Calculate nth Fibonacci number
5. `is_palindrome`: Check if string is palindrome
6. `merge_sorted_arrays`: Merge two sorted arrays
7. `validate_password`: Validate password complexity
8. `cash_register`: Calculate change in ZAR (R50, R20, R10, R5, R2, R1, 50c, 20c, 10c)
9. `are_anagrams`: Check for anagrams
10. `longest_common_prefix`: Find common prefix
11. `evaluate_expression`: Evaluate arithmetic expression
12. `find_duplicates`: Find duplicates in array
13. `print_pascal_triangle`: Generate Pascal's triangle
14. `print_diamond_pattern`: Generate diamond pattern
15. `factorial`: Calculate factorial

Each function has a TODO comment for your implementation.

## Requirements
- Python 3.8+
- No external dependencies

## How to Run Tests
1. Clone the repository
2. Create a branch: `git checkout -b your-branch-name`
3. Implement solutions in `solutions.py`
4. Run tests locally:
```bash
python -m unittest test_solutions.py
```
5. Commit and push your branch
6. Create a pull request to main

## GitHub Actions
- Pull Rquests trigger a workflow running all unit tests
- All tests must pass for Pull Request approval

## Development Guidelines
- Do not modify test file
- Implement functions as specified

These challenges cover algorithms, string manipulation, pattern printing, and practical applications like currency handling.

Good luck!
