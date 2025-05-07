# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        pos=[]
        for i in range(len(grid)):
            grid[i].sort()
            if limits[i] !=0:
                for j in grid[i][-(limits[i]):]:
                    heapq.heappush(pos,j)
                    if len(pos) > k:
                        heapq.heappop(pos)

    
        return sum(pos)