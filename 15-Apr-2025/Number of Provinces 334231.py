# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count=0
        visited=set()
        
        def dfs(node):
            for neighbor in range(len(isConnected)):
                if isConnected[node][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for i in range(len(isConnected)) :
            if i not in visited:
                visited.add(i)
                dfs(i)
                count+=1

        return count

