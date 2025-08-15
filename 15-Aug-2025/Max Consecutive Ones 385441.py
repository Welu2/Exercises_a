# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=0
        c=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
            else:
                m=max(m,c)
                c=0

        return max(m,c)
        