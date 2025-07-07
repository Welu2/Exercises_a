# Problem: Unique Paths III - https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total_squares = 0
        start_x = start_y = 0

        # 1. Count non-obstacle squares and find the start
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != -1:
                    total_squares += 1
                if grid[i][j] == 1:
                    start_x, start_y = i, j

        def dfs(x, y, visited_count):
            # Boundary or obstacle or already visited
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == -1:
                return 0
            if grid[x][y] == -99:  # visited
                return 0

            # If we reached the end
            if grid[x][y] == 2:
                return 1 if visited_count == total_squares else 0

            # Mark current cell as visited
            temp = grid[x][y]
            grid[x][y] = -99  # mark visited

            paths = (
                dfs(x + 1, y, visited_count + 1) +
                dfs(x - 1, y, visited_count + 1) +
                dfs(x, y + 1, visited_count + 1) +
                dfs(x, y - 1, visited_count + 1)
            )

            grid[x][y] = temp  # backtrack
            return paths

        return dfs(start_x, start_y, 1)
            