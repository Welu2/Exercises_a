# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s3 = Counter(s1)
        k = len(s1)
        for i in range(len(s2)- k + 1):
            s4 = Counter(s2[i:k+i])
            if s3 == s4:
                return True
            
        return False