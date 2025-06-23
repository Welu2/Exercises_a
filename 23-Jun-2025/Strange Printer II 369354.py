# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])
        colors = set()
        bounds = {}

        # Step 1: Compute bounding rectangle for each color
        for r in range(m):
            for c in range(n):
                color = targetGrid[r][c]
                colors.add(color)
                if color not in bounds:
                    bounds[color] = [r, r, c, c]  # min_row, max_row, min_col, max_col
                else:
                    bounds[color][0] = min(bounds[color][0], r)
                    bounds[color][1] = max(bounds[color][1], r)
                    bounds[color][2] = min(bounds[color][2], c)
                    bounds[color][3] = max(bounds[color][3], c)

        # Step 2: Build dependency graph
        graph = defaultdict(set)
        indegree = defaultdict(int)
        
        for color in colors:
            min_r, max_r, min_c, max_c = bounds[color]
            for r in range(min_r, max_r + 1):
                for c in range(min_c, max_c + 1):
                    if targetGrid[r][c] != color:
                        other = targetGrid[r][c]
                        if other not in graph[color]:
                            graph[color].add(other)
                            indegree[other] += 1

        # Step 3: Topological sort
        queue = deque()
        for color in colors:
            if indegree[color] == 0:
                queue.append(color)

        count = 0
        while queue:
            current = queue.popleft()
            count += 1
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return count == len(colors)