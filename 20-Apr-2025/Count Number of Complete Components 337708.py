# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        count=0
        visited=set()
        graph=defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, nodes, edge_count):
            nodes.append(node)
            for neighbor in graph[node]:
                edge_count[0]+=1
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor,nodes,edge_count)

        for i in range(n) :
            if i not in visited:
                visited.add(i)
                nodes=[]
                edge_count=[0]
                dfs(i,nodes,edge_count)
                
                
                total_nodes = len(nodes)
                total_edges = edge_count[0] // 2 
                if total_edges == total_nodes * (total_nodes - 1) // 2:
                    count += 1

        return count
