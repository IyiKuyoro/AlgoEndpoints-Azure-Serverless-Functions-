import re
import json
import logging
import azure.functions as func
import numpy as np

from math import floor
from ..SharedCode.error_response_body import error_response_body
from ..SharedCode.success_response_body import success_response_body

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

def main(req: func.HttpRequest) -> func.HttpResponse:
    req_body = req.get_json()
    logging.info(f'Sudoku Function triggered... with "{json.dumps(req_body)}"')

    try:
        sudoku_board = parse_board(req_body.get('board'))

        solver = sudoku_solver(sudoku_board)
        res = success_response_body('Here is the result')
        logging.info(solver())
        res.add_data(solver().tostring())
        return func.HttpResponse(
            str(res),
            status_code=200,
            mimetype="application/json",
        )
    except Exception as ex:
        logging.error(ex)
        res = error_response_body('Server error')
        return func.HttpResponse(
            str(res),
            status_code=500,
            mimetype="application/json",
        )


def parse_board(sudoku_board_string):
    nums = re.split('],\[|\[{2}|]{2}|,', sudoku_board_string)
    arr_nums = [[],[],[],[],[],[],[],[],[]]

    col = 0
    row = 0
    for num in nums:
        if num:
            num = int(num)
            if num < 0 or num > 9 :
                raise Exception("Only single digit positive integers are permitted in sudoku.")

            arr_nums[row].append(num)
            col += 1
            if col > 8:
                col = 0
                row += 1
            if row > 8:
                return arr_nums

    return arr_nums
