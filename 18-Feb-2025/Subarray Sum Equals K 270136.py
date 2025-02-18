# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        cursum=0
        sumdict=defaultdict(int)
        sumdict[0]=1
        for num in nums:
            cursum+=num
            
            count+=sumdict[cursum-k]
            sumdict[cursum]+=1

        return count
