# Problem: Count Subarrays Where Max Element Appears at Least K Times - https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxE=max(nums)
        numbers=defaultdict(int)
        c=0
        l=0
        for r in range(len(nums)):
            numbers[nums[r]]+=1
            while numbers[maxE]>= k:
                c+=len(nums)-r
                numbers[nums[l]]-=1
                l+=1
        
        
        return c
