# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans=0
        pos=set()
        
        def digitsum(i,path,l):
            nonlocal ans
            if not l:
                if sum(path) == i and i**2 not in pos:
                    ans+=i**2
                    pos.add(i**2)
            for j in range(1,len(l)+1):
                path.append(int(l[:j]))
                digitsum(i,path,l[j:])
                path.pop()
        for i in range(1,n+1):
            digitsum(i,[],str(i**2))
        return ans
         
            