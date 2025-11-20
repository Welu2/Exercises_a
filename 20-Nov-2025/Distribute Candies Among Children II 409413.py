# Problem: Distribute Candies Among Children II - https://leetcode.com/problems/distribute-candies-among-children-ii/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def C2(k):
            return (k * (k - 1)) // 2 if k >= 2 else 0
        
        total = (
            C2(n + 2)
            - 3 * C2(n - limit + 1)
            + 3 * C2(n - 2 * limit)
            - C2(n - 3 * limit - 1)
        )
        
        return max(total, 0)