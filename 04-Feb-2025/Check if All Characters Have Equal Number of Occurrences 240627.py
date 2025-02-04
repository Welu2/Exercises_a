# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a=Counter(s)
        b=[]
        for i in a:
            b.append(a[i])

        if len(set(b))==1:
            return True
        return False
        