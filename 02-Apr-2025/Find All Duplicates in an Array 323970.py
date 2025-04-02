# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a=[]
        b=Counter(nums)
        for i in b:
            if b[i] >1:
                a.append(i)

        return a