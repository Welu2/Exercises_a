# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n=len(nums)
        prefix=[0]*(n)
        for start,end in requests:
            prefix[start]+=1
            if end+1 < n:
                prefix[end+1] -=1
        

        for j in range(1,n):
            prefix[j]+=prefix[j-1]
      
        nums.sort()
        prefix.sort()
        modulus = 10**9 + 7
        total =sum(num*freq for num,freq in zip(nums,prefix))
        return total % modulus

        