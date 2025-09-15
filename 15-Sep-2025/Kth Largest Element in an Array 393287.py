# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a=0
        d=[]
        for i in nums:
            d.append(-i)

        heapq.heapify(d)

        while k>0:
           a= heapq.heappop(d)
           k-=1

        return -a
        
        