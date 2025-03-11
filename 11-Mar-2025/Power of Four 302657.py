# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        c = 0
        no=n
        while no > 1:
            no//=4
            c+=1

        return n == (4**c)
