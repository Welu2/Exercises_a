# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low=1
        high=max(candies)
        def check(mid):
            child=0
            for i in candies:
                if i >= mid:
                    child+=(i//mid)
                    
            return child >= k
        if k > sum(candies):
            return 0
        candy=0
        while low <= high:
            mid=(low+high)//2
            if check(mid):
                candy=mid
                low=mid+1
            else:
                high=mid-1

        return candy

