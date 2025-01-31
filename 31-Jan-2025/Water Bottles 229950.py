# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk=0
        while numBottles >= numExchange:
            numBottles-=numExchange
            drunk+=numExchange
            numBottles+=1

        return drunk+numBottles