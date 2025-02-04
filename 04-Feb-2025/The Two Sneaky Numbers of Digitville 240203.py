# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a=[]
        b=Counter(nums)
        for i in b:
            if b[i]>1:
                a.append(i)
            
        return a
