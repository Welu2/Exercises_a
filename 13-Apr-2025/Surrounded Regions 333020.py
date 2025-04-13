# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'T'  # Temporarily mark
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        # 1. Mark the 'O's on the borders and their connected regions
        for r in range(rows):
            for c in [0, cols - 1]:
                if board[r][c] == 'O':
                    dfs(r, c)
        for r in [0, rows - 1]:
            for c in range(cols):
                if board[r][c] == 'O':
                    dfs(r, c)

        # 2. Flip all remaining 'O' to 'X', and 'T' back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
