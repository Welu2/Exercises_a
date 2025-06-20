# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(row, col, diagonals, anti_diagonals, cols):
            return col not in cols and (row - col) not in diagonals and (row + col) not in anti_diagonals

        def backtrack(row, diagonals, anti_diagonals, cols, state):
            if row == n:
                board = []
                for r in state:
                    board.append("." * r + "Q" + "." * (n - r - 1))
                res.append(board)
                return

            for col in range(n):
                if is_valid(row, col, diagonals, anti_diagonals, cols):
                    cols.add(col)
                    diagonals.add(row - col)
                    anti_diagonals.add(row + col)
                    state.append(col)

                    backtrack(row + 1, diagonals, anti_diagonals, cols, state)

                    # backtrack
                    cols.remove(col)
                    diagonals.remove(row - col)
                    anti_diagonals.remove(row + col)
                    state.pop()

        res = []
        backtrack(0, set(), set(), set(), [])
        return res