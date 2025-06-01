# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        m=0
        l=0
        c=0
        for i in range(len(nums)):
            if nums[i]==0:
                c+=1
    
            while c>k:
                if nums[l] == 0:
                    c-=1
                l+=1
            m=max(m,(i-l)+1)

        return m
