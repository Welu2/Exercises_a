# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isSet(values):
            non_empty = [val for val in values if val != '.']
            return len(set(non_empty)) == len(non_empty)
        for row in board:
            if not isSet(row):
                return False
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not isSet(column):
                return False
        for row in range(0, 9, 3):  # Start row of each 3x3 sub-grid
            for col in range(0, 9, 3):  # Start column of each 3x3 sub-grid
                subgrid = []
                for i in range(3):
                    for j in range(3):
                        subgrid.append(board[row + i][col + j])
                if not isSet(subgrid):
                    return False
        
        return True
        
        