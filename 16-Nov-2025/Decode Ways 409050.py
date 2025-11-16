# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        
        dp[0] = 1  # empty string
        dp[1] = 0 if s[0] == '0' else 1  # first character
        
        for i in range(2, n + 1):
            # One-digit decode
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # Two-digit decode
            two = int(s[i-2:i])
            if 10 <= two <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]
