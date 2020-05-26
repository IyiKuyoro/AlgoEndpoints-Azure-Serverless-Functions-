import numpy as np
from math import floor

class sudoku_solver:

    def __init__(self, board):
        self._board = np.array(board)
        self._empty_cells = []

    def __call__(self):
        self._solve()
        return self._board

    def _compute_possibilities(self):
        board_transposed = np.transpose(self._board)
        empty_cells = []

        for i in range(0, 9):
            for j in range(0, 9):
                if self._board[i][j] == 0:
                    empty_cells.append([i, j, [1, 2, 3, 4, 5, 6, 7, 8, 9]])

        for v in empty_cells:
            row = v[0]
            col = v[1]
            arr = v[2]
            row_idx =  floor(row / 3) * 3
            col_idx = floor(col / 3) * 3
            cell = self._board[
                row_idx:row_idx + 3,
                col_idx:col_idx + 3
            ]
            possibleNums = [
                num for num in arr
                if num not in self._board[row]
                and num not in board_transposed[col]
                and num not in cell
            ]
            v[2] = possibleNums

        return empty_cells

    def _solve(self):
        empty_cells = sorted(self._compute_possibilities(), key=lambda element: len(element[2]))

        if len(empty_cells) <= 0:
            return True

        row = empty_cells[0][0]
        col = empty_cells[0][1]
        values = empty_cells[0][2]
        if len(values) > 0:
            i = 0
            loop = True
            while loop and i < len(values):
                pos_value = values[i]
                self._board[row][col] = pos_value
                loop = not self._solve()

                if loop == True:
                    self._board[row][col] = 0
                else:
                    return True

                i += 1

                if i >= len(values):
                    return False
        elif len(values) == 0:
            return False

        return True
