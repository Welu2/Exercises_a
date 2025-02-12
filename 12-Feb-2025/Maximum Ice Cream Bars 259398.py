# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        l=0
        total=0
        while l < len(costs)  :
            
            total+=costs[l]
            if total > coins:
                break
            l+=1
        return l
