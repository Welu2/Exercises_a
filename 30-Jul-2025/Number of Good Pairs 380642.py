# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a=Counter(nums)
        c=0
        def no(n):
            return (n * (n - 1)) // 2

        for i in a:
            if a[i] > 1:
                c+= no(a[i])

        return c
