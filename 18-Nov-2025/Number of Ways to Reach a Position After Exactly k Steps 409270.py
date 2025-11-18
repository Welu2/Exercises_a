# Problem: Number of Ways to Reach a Position After Exactly k Steps - https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if abs(endPos - startPos) > k or (k - abs(endPos - startPos)) % 2 != 0:
            return 0
        MOD = 10**9 + 7
        dp = {}
        dp[startPos] = 1

        for step in range(k):
            next_dp = {}
            for pos in dp:
                if pos + 1 not in next_dp:
                    next_dp[pos + 1] = 0
                if pos - 1 not in next_dp:
                    next_dp[pos - 1] = 0
                next_dp[pos + 1] = (next_dp[pos + 1] + dp[pos]) % MOD
                next_dp[pos - 1] = (next_dp[pos - 1] + dp[pos]) % MOD
            dp = next_dp

        return dp.get(endPos, 0)