# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = nums.count(0)
        y = nums.count(1)
        for i in range(len(nums)):
            if i < x:
                nums[i] = 0
            elif x <= i < x+y:
                nums[i] = 1
            else:
                nums[i] = 2
                
