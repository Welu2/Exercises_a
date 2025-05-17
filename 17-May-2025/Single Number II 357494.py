# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=Counter(nums)
        for key in c:
            if c[key] == 1:
                return key

        