# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        grey=0
        white=1
        black=2
        color={c:grey for c in range(1,n+1) }
        adj_list=defaultdict(list)
        for a,b in dislikes:
            adj_list[a].append(b)
            adj_list[b].append(a)
        is_possible=True
        def dfs(node,c):
            nonlocal is_possible
            if not is_possible:
                return
            color[node]=c
            for neigh in adj_list[node]:
                if color[neigh]==0:
                    dfs(neigh,black if c==white else white)
                elif color[neigh]==c:
                    is_possible=False
                    return
            
          
        for i in range(1,n+1):
            if color[i]==0:
                dfs(i,white)
        return is_possible