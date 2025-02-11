# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        mysum=0
        l=0
        for i in piles[len(piles)//3:]:
            if l % 2==0:
                mysum+=i
            l+=1

        return mysum
