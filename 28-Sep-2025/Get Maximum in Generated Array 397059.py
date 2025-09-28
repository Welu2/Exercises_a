# Problem: Get Maximum in Generated Array - https://leetcode.com/problems/get-maximum-in-generated-array/description/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums=[0]*(n+1)
        if n == 0:
            return 0
        nums[0]=0
        nums[1]=1
        for i in range(2,n+1):
            a=i//2
            if i % 2== 0:
                
                nums[i]=nums[a]
            else:
                nums[i]=nums[a]+nums[a+1]
     
        return max(nums)
