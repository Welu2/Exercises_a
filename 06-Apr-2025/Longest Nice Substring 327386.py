# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def isnice(s):
            for i in s:
                if i.upper() not in s or i.lower() not in s:
                    return False
            return True

        
        d=''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                b = s[i:j]
                if isnice(b) and len(b) > len(d):
                    d = b
        return d