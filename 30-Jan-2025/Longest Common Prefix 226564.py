# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=1
        c=''
        
        while l<= len(strs[0]):
            if all(strs[0][:l] == x[:l] for x in strs):
                c+=strs[0][l-1]
                l+=1
                
            else:
                break
        return c
