# Problem: Array With Elements Not Equal to Average of Neighbors - https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = [0] * len(nums)
        mid = (len(nums) + 1) // 2
        small = nums[:mid]
        large = nums[mid:]
        
        # Place smaller elements at even indices
        result[::2] = small
        # Place larger elements at odd indices
        result[1::2] = large
        return result