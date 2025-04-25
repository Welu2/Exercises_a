# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        Reversedgraph=[[] for j in range(len(graph))]
        queue=deque()
        ans=[]
        for i in range(len(graph)):
            for node in graph[i]:
                Reversedgraph[node].append(i)

        out_degree = [0 for _ in range(len(graph))]
        for i in range(len(graph)):
            out_degree[i]=len(graph[i])

        for d in range(len(out_degree)):
            if out_degree[d] == 0:
                queue.append(d)

        while queue:
            node=queue.popleft()
            ans.append(node)
            for n in Reversedgraph[node]:
                out_degree[n]-=1
                if out_degree[n] == 0:
                    queue.append(n)

        ans.sort()
        return ans


