# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        minV=nums[0]
        for i in nums[1:]:
            while stack and stack[-1][0] <= i:
                stack.pop()
            
            if stack and stack[-1][1] < i:
                return True
            stack.append([i,minV])
            minV=min(minV,i)
            
            
        return False