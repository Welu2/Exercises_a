# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
    
    # Check if a valid partition is possible
        if (target + total_sum) % 2 != 0 or total_sum < abs(target):
            return 0
        
        S = (target + total_sum) // 2
        
        dp = [0] * (S + 1)
        dp[0] = 1
        
        for num in nums:
            for i in range(S, num - 1, -1):
                dp[i] += dp[i - num]
        
        return dp[S]