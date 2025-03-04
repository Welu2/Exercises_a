# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left=0
        L_count=0
        balanced=0
        while left < len(s):
            if s[left] == 'L':
                L_count+=1
            else:
                L_count-=1
            if L_count==0:
                balanced+=1
            left+=1

        return balanced
            