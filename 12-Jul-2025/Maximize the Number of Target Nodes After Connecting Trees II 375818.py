# Problem: Maximize the Number of Target Nodes After Connecting Trees II - https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def build_graph(n, edges):
            g = [[] for _ in range(n)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            return g

        def bfs_color(n, g):
            par = [-1]*n
            cnt = [0, 0]
            q = deque([0])
            par[0] = 0
            cnt[0] = 1
            while q:
                u = q.popleft()
                for v in g[u]:
                    if par[v] == -1:
                        par[v] = par[u]^1
                        cnt[par[v]] += 1
                        q.append(v)
            return par, cnt

        n = len(edges1) + 1
        m = len(edges2) + 1
        g1 = build_graph(n, edges1)
        g2 = build_graph(m, edges2)

        par1, cnt1 = bfs_color(n, g1)
        par2, cnt2 = bfs_color(m, g2)

        base2 = max(cnt2)
        ans = [cnt1[par1[i]] + base2 for i in range(n)]
        return ans
            