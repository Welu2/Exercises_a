# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        edges=[]
        for i in range(len(s1)):
            edges.append([s1[i],s2[i]])
            
        parent = {chr(i): chr(i) for i in range(97, 123)}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            X=find(x)
            Y=find(y)
            if X == Y:
                return
            else:
                if X < Y:
                    parent[Y] = X     
                else:
                    parent[X] = Y
                    

        ans=[]
        for u,v in edges:
            union(u,v)
        for i in baseStr:
            ans.append(find(i))

        return "".join(ans)
