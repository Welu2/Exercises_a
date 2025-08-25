# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = len(word1)
        b = len(word2)
        c = ""
        y = min(a,b) 
        
        for v in range(y):
            c += word1[v]
            c += word2[v]
        
        if a > b:
            c += word1[y:]
        elif b > a:
            c += word2[y:]
                     
        return c
                    




