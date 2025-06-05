# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxi = 0
        i = 1
        if len(s) == len(set(s)):
            return len(s)
        while i <= len(s):
            d = s[l:i]
            if len(d) > len(set(d)):
                l += 1
            elif len(d) == len(set(d)):
                maxi = max(maxi,len(d))
                i += 1
        
    
        return maxi
                
        