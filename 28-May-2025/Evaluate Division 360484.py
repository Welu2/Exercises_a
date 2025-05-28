# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
    
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val
        
        # Step 2: Function to perform DFS
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, weight in graph[start].items():
                if neighbor in visited:
                    continue
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return result * weight
            return -1.0
        
        # Step 3: Evaluate each query
        results = []
        for a, b in queries:
            results.append(dfs(a, b, set()))
        
        return results