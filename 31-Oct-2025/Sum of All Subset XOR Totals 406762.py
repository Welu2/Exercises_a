# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans=0
        res = []

        def backtrack(start, path):
            res.append(path[:])  

            for i in range(start, len(nums)):
                path.append(nums[i])         
                backtrack(i + 1, path)        
                path.pop()                    

        backtrack(0, [])
        def x_o_r(s):
            l=0
            for i in s:
                l^=i
            return l
        for j in res:
            ans+=x_o_r(j)
        return ans



