# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []
        
        min_heap = []
        result = []

        # Initialize heap with the smallest pairs: (nums1[0] + nums2[j], 0, j)
        for j in range(min(k, len(nums2))):
            heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))
        
        while min_heap and len(result) < k:
            total, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            
            # If possible, push the next pair (i+1, j)
            if i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i+1] + nums2[j], i+1, j))
        
        return result