# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and trust==[]:
            return 1
        a=defaultdict(int)
        known=set()
        flag=False
        for t in trust:
            a[t[1]]+=1
            if a[t[1]] == n-1:
                flag=True
            known.add(t[0])

        if flag:
            for j in range(1,n+1):
                if j not in known:
                    return j
    
        return -1
        
        