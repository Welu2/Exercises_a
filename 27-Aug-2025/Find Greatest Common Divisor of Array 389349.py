# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=1
        mi=min(nums)
        ma=max(nums)
        for i in range(2,mi+1):
            if ma%i ==0 and mi % i ==0:
                a=i

        return a
        