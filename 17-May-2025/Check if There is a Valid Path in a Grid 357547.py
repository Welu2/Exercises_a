# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        # Map of directions: (row_change, col_change)
        directions = {
            1: [(0, -1), (0, 1)],     # left, right
            2: [(-1, 0), (1, 0)],     # up, down
            3: [(0, -1), (1, 0)],     # left, down
            4: [(0, 1), (1, 0)],      # right, down
            5: [(0, -1), (-1, 0)],    # left, up
            6: [(0, 1), (-1, 0)]      # right, up
        }

        # Map to find opposite directions
        opposites = {
            (0, -1): (0, 1),
            (0, 1): (0, -1),
            (-1, 0): (1, 0),
            (1, 0): (-1, 0)
        }

        visited = [[False]*n for _ in range(m)]
        queue = deque([(0, 0)])
        visited[0][0] = True

        while queue:
            r, c = queue.popleft()
            if r == m - 1 and c == n - 1:
                return True
            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    if opposites[(dr, dc)] in directions[grid[nr][nc]]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
        return False