# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        a=0
        m=a
        c=Counter()
        for i in range(k):
            a+=nums[i]
            c[nums[i]]+=1
        
        if len(c)==k:
            m=max(m,a)

        for j in range(k,len(nums)):
            c[nums[j-k]]-=1
            if c[nums[j-k]] ==0:
                del c[nums[j-k]]

            c[nums[j]]+=1
            a+=nums[j] -nums[j-k]
            if len(c)==k:
                m=max(m,a)

        return m
