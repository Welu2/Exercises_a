# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sq=int(sqrt(c))
        
        if sq*sq == c:
            return True
        l=1
        r=sq
        while l <= r:
            sum_sq=(l**2) + (r**2)
            if sum_sq == c:
                return True
            elif sum_sq < c:
                l+=1
            else:
                r-=1

        return False