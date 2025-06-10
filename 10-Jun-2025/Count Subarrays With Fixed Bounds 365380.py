# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        last_min = last_max = last_invalid = -1

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                last_invalid = i
            if num == minK:
                last_min = i
            if num == maxK:
                last_max = i

            valid_start = min(last_min, last_max)
            res += max(0, valid_start - last_invalid)

        return res