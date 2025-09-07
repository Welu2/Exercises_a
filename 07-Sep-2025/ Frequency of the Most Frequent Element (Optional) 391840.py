# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        max_freq = 0

        for right in range(len(nums)):
            total += nums[right]

            # Shrink window if total operations exceed k
            while nums[right] * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1

            max_freq = max(max_freq, right - left + 1)

        return max_freq