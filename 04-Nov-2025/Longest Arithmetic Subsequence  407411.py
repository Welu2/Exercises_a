# Problem: Longest Arithmetic Subsequence  - https://leetcode.com/problems/longest-arithmetic-subsequence/

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [dict() for _ in range(n)]  # dp[i][diff] = length ending at i with diff
        longest = 0

        for j in range(n):
            for i in range(j):
                diff = nums[j] - nums[i]
                dp[j][diff] = dp[i].get(diff, 1) + 1
                longest = max(longest, dp[j][diff])

        return longest