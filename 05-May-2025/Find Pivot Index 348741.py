# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
       lsum=0
       rsum=sum(nums)
       for i in range(len(nums)):
        rsum-=nums[i]
        if rsum==lsum:
            return i
        lsum+=nums[i]

    
    
       return -1
