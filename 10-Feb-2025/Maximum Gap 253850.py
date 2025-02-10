# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        m=0
        l=0
        for i in range(1,len(nums)):
            m=max(m,nums[i]-nums[l])
            l+=1
        
        return m
        