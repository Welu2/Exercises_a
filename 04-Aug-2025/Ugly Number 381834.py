# Problem: Ugly Number - https://leetcode.com/problems/ugly-number/description/

class Solution:
    def isUgly(self, n: int) -> bool:
        pos =(2,3,5)
        i = 2
        if n == 1:
            return True
        if n <= 0:
            return False
        while i * i <= n:
            if n % i == 0:
                if i not in pos:
                    return False
                while n % i == 0:
                    n //= i
            i += 1
        
        if n not in pos and n > 1:
            return False
       
        return True