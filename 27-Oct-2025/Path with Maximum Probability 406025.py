# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (a, b), p in zip(edges, succProb):
            graph[a].append((b, p))
            graph[b].append((a, p))
        
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0
        
        heap = [(-1.0, start_node)]  # use negative for max heap
        
        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob
            
            if node == end_node:
                return prob
            
            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))
        
        return 0.0