# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=[prices[0]]
        m=0
        for i in range(1,len(prices)):
            if a and a[-1] > prices[i]:
                a.pop()
                a.append(prices[i])
            elif a:
                m= max(m,(prices[i]-a[-1]))

        return m


            