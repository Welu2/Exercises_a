# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = []

       
        for i in range(n):
            heapq.heappush(m, (matrix[i][0], i, 0))

       
        for _ in range(k - 1):
            val, r, c = heapq.heappop(m)

           
            if c + 1 < n:
                heapq.heappush(m, (matrix[r][c + 1], r, c + 1))

       
        return heapq.heappop(m)[0]