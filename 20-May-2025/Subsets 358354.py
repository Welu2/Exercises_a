# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
    
        for i in range(1 << n):  # from 0 to 2^n - 1
            subset = []
            for j in range(n):
                if i & (1 << j):  # if j-th bit is set
                    subset.append(nums[j])
            result.append(subset)
        
        return result
    
        

        

        