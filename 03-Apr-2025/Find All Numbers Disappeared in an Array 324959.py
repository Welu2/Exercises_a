# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(1,len(nums)+1):
            a.append(i)
        
        a = set(a)
        b=set(nums)
        c= a.difference(b)
        d=list(c)

        return d
        