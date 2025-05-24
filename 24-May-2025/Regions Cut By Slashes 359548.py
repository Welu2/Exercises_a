# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        size = n * 3
        g = [[0] * size for _ in range(size)]

        for i in range(n):
            for j in range(n):
                c = grid[i][j]
                r, c3 = i * 3, j * 3
                if c == '/':
                    g[r][c3 + 2] = 1
                    g[r + 1][c3 + 1] = 1
                    g[r + 2][c3] = 1
                elif c == '\\':
                    g[r][c3] = 1
                    g[r + 1][c3 + 1] = 1
                    g[r + 2][c3 + 2] = 1

        def dfs(x, y):
            if x < 0 or y < 0 or x >= size or y >= size or g[x][y] != 0:
                return
            g[x][y] = 2  # mark as visited
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x + dx, y + dy)

        regions = 0
        for i in range(size):
            for j in range(size):
                if g[i][j] == 0:
                    dfs(i, j)
                    regions += 1

        return regions
