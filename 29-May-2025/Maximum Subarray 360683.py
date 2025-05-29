# Problem: Maximum Subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runing=nums[0]
        maxS=nums[0]
        cursum=0
        for i in range(1,len(nums)):
            runing+=nums[i]
            runing=max(runing,nums[i])
            maxS=max(maxS,runing)

        return maxS


