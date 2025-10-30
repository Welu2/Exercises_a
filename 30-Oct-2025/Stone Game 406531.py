# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        
        # Base case: when there's only one pile left
        for i in range(n):
            dp[i][i] = piles[i]
        
        # Fill DP table
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        
        # If Alice's score difference > 0, she wins
        return dp[0][n-1] > 0