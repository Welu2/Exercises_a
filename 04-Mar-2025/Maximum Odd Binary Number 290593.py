# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        counter=Counter(s)
        result=[]
        ones=counter['1']
        zeros=counter['0']
        while ones > 1:
            result.append('1')
            ones-=1
        while zeros >0:
            result.append('0')
            zeros-=1
        result.append('1')
        return "".join(result)
        