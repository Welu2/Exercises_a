# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
      
        f = [1] * n
      
        for i in range(1, n):
            
            if nums[i] == nums[i - 1] + 1:
      
                f[i] = f[i - 1] + 1
     
        return [nums[i] if f[i] >= k else -1 for i in range(k - 1, n)]