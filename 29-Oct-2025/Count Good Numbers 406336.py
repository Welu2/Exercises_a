# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Fast modular exponentiation
        def power(base, exp):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return result
        
        even_count = (n + 1) // 2
        odd_count = n // 2
        
        return (power(5, even_count) * power(4, odd_count)) % MOD