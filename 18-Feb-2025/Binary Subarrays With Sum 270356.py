# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cursum=0
        dic=defaultdict(int)
        dic[0]=1
        count=0
        for num in nums:
            cursum+=num
            count+=dic[cursum-goal]
            dic[cursum]+=1
        return count
