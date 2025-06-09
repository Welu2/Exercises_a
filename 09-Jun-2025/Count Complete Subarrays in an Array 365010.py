# Problem: Count Complete Subarrays in an Array - https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
      a=len(set(nums))
      c=0
      l=0
      r=1
      if len(set(nums))==1:
        c+=1
      while r < len(nums):
        b=len(set(nums[l:r+1]))
        if b ==a:
            c+=((len(nums)-r))
            l+=1
        else:
            r+=1
      return c