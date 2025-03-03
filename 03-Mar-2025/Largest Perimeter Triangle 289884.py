# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        use =[0]
        sum = 0
        for k in range(len(nums) - 2):
          if nums[k + 2] < (nums[k] + nums[k + 1]):
            sum = nums[k] + nums[k + 1] + nums[k+ 2]
            use.append(sum)


        return (max(use))
          
