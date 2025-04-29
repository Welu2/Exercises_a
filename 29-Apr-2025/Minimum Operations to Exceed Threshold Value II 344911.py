# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        c=0
        if nums[0] >= k:
                return c
        while c <= k and len(nums) >= 2:
            
            x=heapq.heappop(nums)
            y=heapq.heappop(nums)

          
            n=min(x,y)*2+max(x,y)
            heapq.heappush(nums, n)
            

            c+=1
            if nums[0] >= k:
                return c
