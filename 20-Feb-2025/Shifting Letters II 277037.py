# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix=[0]*(len(s)+1)
        for start,end,flow in shifts:
            value=1 if flow == 1 else -1
            prefix[start]+=value
            prefix[end+1]-=value
        
        for i in range(1,len(s)+1):
            prefix[i]+=prefix[i-1]
       
        changed=[]
        for i in range(len(s)):
            changed.append(chr(ord('a') + (ord(s[i]) - ord('a') + prefix[i] + 26) % 26) )
        return "".join(changed)


        