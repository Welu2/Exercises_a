# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a=[]
        b=Counter(nums)
        for i in b:
            if b[i]==1:
                a.append(i)

        return a 
        