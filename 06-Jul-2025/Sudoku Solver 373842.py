# Problem: Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Pre-fill sets and collect empty cells
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == '.':
                    empty_cells.append((i, j))
                else:
                    rows[i].add(cell)
                    cols[j].add(cell)
                    boxes[(i // 3) * 3 + (j // 3)].add(cell)

        def backtrack(index: int = 0) -> bool:
            if index == len(empty_cells):
                return True  # All cells filled

            row, col = empty_cells[index]
            box_idx = (row // 3) * 3 + (col // 3)

            for num in map(str, range(1, 10)):
                if num not in rows[row] and num not in cols[col] and num not in boxes[box_idx]:
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box_idx].add(num)

                    if backtrack(index + 1):
                        return True

                    # Undo
                    board[row][col] = '.'
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box_idx].remove(num)

            return False

        backtrack()