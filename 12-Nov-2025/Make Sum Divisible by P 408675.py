# Problem: Make Sum Divisible by P - https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rem = total % p
        if rem == 0:
            return 0  # already divisible

        prefix = 0
        seen = {0: -1}  # prefix mod value → index
        res = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - rem + p) % p

            if target in seen:
                res = min(res, i - seen[target])

            seen[prefix] = i  # update last occurrence

        return res if res < len(nums) else -1