# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, rank, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            if root_x == root_y:
                return False
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            return True

     
        edges = [[t, u-1, v-1] for t, u, v in edges]

        parent_a = list(range(n))
        rank_a = [0] * n
        parent_b = list(range(n))
        rank_b = [0] * n

        removed = 0
        used_a = used_b = 0

            # Type 3 edges (shared)
        for t, u, v in edges:
            if t == 3:
                a = union(parent_a, rank_a, u, v)
                b = union(parent_b, rank_b, u, v)
                if a: used_a += 1
                if b: used_b += 1
                if not a and not b:
                    removed += 1

            # Type 1 edges (Alice only)
        for t, u, v in edges:
            if t == 1:
                if union(parent_a, rank_a, u, v):
                    used_a += 1
                else:
                    removed += 1

            # Type 2 edges (Bob only)
        for t, u, v in edges:
            if t == 2:
                if union(parent_b, rank_b, u, v):
                    used_b += 1
                else:
                    removed += 1

            # Final check: both must have n-1 edges to be fully connected
        if used_a != n - 1 or used_b != n - 1:
            return -1
        return removed