# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        z_index=[]
        
        for i in range(len(s)):
            if s[i] == '0':
                z_index.append(i)
        zeros=s.count('0')
        total=0
        for j in range(zeros):
            total+=z_index[j]-j

        return total