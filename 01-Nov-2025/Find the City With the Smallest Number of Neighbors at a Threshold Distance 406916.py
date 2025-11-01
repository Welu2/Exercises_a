# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = float('inf')
        dist = [[INF] * n for _ in range(n)]
        
        # Distance to self = 0
        for i in range(n):
            dist[i][i] = 0

        # Step 2: Fill in given edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w  # since bidirectional

        # Step 3: Floyd-Warshall all-pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Step 4: Count reachable cities for each node
        min_reachable = n  # start with max possible
        result_city = -1

        for i in range(n):
            count = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
            
            # If fewer reachable cities, or tie → take larger index
            if count < min_reachable or (count == min_reachable and i > result_city):
                min_reachable = count
                result_city = i

        return result_city
            