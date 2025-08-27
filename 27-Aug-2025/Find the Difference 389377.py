# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(s)
        d = Counter(t)
        
        for key in d:
            if key not in s or c[key] != d[key]:
                return key
            
       