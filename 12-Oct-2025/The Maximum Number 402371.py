# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a=[]
        d=0
        k=3
        for i in set(nums):
            a.append(-i)

        heapq.heapify(a)
        if k > len(set(nums)):
            return -(heapq.heappop(a))

        while k>0:
            d= heapq.heappop(a)
            k-=1

        return -d

        