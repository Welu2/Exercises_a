# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
    
        cache = [[0] * n for _ in range(m)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            if cache[i][j] != 0:
                return cache[i][j]
            
            max_len = 1 
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    length = 1 + dfs(x, y)
                    max_len = max(max_len, length)

            cache[i][j] = max_len
            return max_len

        return max(dfs(i, j) for i in range(m) for j in range(n))