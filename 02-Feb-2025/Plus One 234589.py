# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        v = ''.join(map(str,digits))
        b=int(v)
        c=list(str(b+1))
        digits = [int(digit) for digit in c]

        return digits