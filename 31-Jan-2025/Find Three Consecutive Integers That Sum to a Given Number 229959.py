# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        a=num-3 
        if a % 3 ==0:
            b=a//3
            return[b,b+1,b+2]
        return []
