# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        w={}
        for i in range(len(s)):
            w[s[i]] = t[i]

       
        words=""
        for j in s:
            words+=w[j]

        if  len(set(s))!=len(set(t)):
            return False
        return t == words 
        