## Sudoku Solver

This function helps to solve a sudoku challenge. Passing in your unsolved sudoku matrix and it will do its magic.

### How to use:

- The URL for this endpoint is `baseURL`/api/SudokuFunction. It accepts only [GET] requests. All other methods will return 404.
- The function is expecting a json content type.
- In the body of the [POST] request, add a single parameter called `board`
- The `board` parameter is a string representation of a matrix with the following constrains:
  - Only single digit integers, open and close square brackets and commas are allowed. All other characters will be sanitized.
  - The function is expecting 81 integers. Any integer outside that count will not be considered.
  - Use `0` in place of blank sudoku cells.

Eg:
```
"[[9,8,4,0,3,1,0,7,2],[6,1,0,0,0,7,0,0,0],[2,5,7,0,0,9,8,0,0],[3,0,0,0,6,0,0,1,0],[0,0,0,3,7,0,9,2,0],[0,0,9,0,0,5,0,0,0],[0,3,0,0,0,6,0,0,0],[0,4,5,0,1,8,0,9,6],[1,9,6,7,0,0,2,8,0]]"
```
