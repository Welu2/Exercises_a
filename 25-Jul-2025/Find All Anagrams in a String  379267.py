# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a =[]
        target = Counter(p)
        f = len(p)
        for n in range(len(s) - f + 1):
            sub = s[n:f+n] 
            d = Counter(sub)
            if target == d:
                a.append(n)
        

        return a
        