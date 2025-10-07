# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        case=[True for _ in range(n)] 
        if n == 0:
            return 0
        case[0] =  False
        if n > 1:
            case[1] =  False
            
        for i in range(2,int(n**0.5)+1):
            if case[i] == True:
                for multiple in range(i * i, n, i):
                    case[multiple] = False
            
          
        return case.count(True)