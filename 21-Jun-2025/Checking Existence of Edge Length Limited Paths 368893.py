# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])  # Path compression
                return self.parent[x]
            
            def union(self, x, y):
                px = self.find(x)
                py = self.find(y)
                if px != py:
                    self.parent[px] = py

        edgeList.sort(key=lambda x: x[2])  # Sort edges by distance
        indexed_queries = sorted([(limit, u, v, i) for i, (u, v, limit) in enumerate(queries)])
        
        uf = UnionFind(n)
        answer = [False] * len(queries)
        i = 0  # pointer for edgeList
        
        for limit, u, v, query_index in indexed_queries:
            while i < len(edgeList) and edgeList[i][2] < limit:
                uf.union(edgeList[i][0], edgeList[i][1])
                i += 1
            if uf.find(u) == uf.find(v):
                answer[query_index] = True
        
        return answer
    
        
        

            