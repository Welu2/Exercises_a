# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       left = 0
       right = len(nums) - 1
       while left <= right:
        c = target - nums[left]
        b = target - nums[right]
        if c in nums and nums.index(c) != left:
            return [left,nums.index(c)]
        elif b in nums and nums.index(b) != right:
            return [right, nums.index(b)]
        left += 1
        right -= 1