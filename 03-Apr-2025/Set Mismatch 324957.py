# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        a=[]
        for i in d:
            if d[i]>1:
                a.append(i)
        for j in range(1,len(nums)+1):
            if j not in nums:
                a.append(j)
        
        return a
        