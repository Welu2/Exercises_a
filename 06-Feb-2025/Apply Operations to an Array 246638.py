# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i=0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
               
            i+=1
    
        output=[]
        c=0
        for num in nums:
            if num!=0:
                output.append(num)
            else:
                c+=1
        return output+[0]*c
