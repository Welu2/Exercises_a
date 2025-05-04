# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[i for i in range(n+1)]
        rank=[0]*(n+1)

        def find(node):
            while parent[node] != node:
                parent[node]=parent[parent[node]]
                node= parent[node]
            return parent[node] 

        def union(a,b):
            root1=find(a)
            root2=find(b)
            if root1 == root2:
                return False
            if root1 > root2:
                parent[root2]=root1
                rank[root1]+=rank[root2]
            else:
                parent[root1]=root2
                rank[root2]+= rank[root1]
            return True

        for a,b in edges:
            if not union(a,b):
                return [a,b]