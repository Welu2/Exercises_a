# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = max(nums)
        c = 0
        for i in range(a+1):
            if i not in nums:
                c =i
                break
            c = a + 1
        return c
        