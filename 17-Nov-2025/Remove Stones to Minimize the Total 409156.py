# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-num for num in piles]
        heapq.heapify(max_heap)

        for _ in range(k):
            # Get the largest element
            largest = -heapq.heappop(max_heap)
            
        
        # Push the modified element back into the heap
            new_value = floor(largest / 2)
            heapq.heappush(max_heap, -(largest-new_value))

        return -1*sum(max_heap)
        