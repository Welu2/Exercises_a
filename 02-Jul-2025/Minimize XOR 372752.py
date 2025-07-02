# Problem: Minimize XOR - https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        k = bin(num2).count('1')

        result = 0
       
        for i in range(31, -1, -1):  
            if num1 & (1 << i) and k > 0:
                result |= (1 << i)
                k -= 1

        
        for i in range(32):
            if not (result & (1 << i)) and k > 0:
                result |= (1 << i)
                k -= 1

        return result

            