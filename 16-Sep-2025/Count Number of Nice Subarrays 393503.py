# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1  # to handle subarrays starting at index 0

        res = 0
        odd_count = 0

        for num in nums:
            if num % 2 == 1:
                odd_count += 1

            # Check how many times we've seen (odd_count - k) before
            res += count[odd_count - k]
            
            # Record this odd_count
            count[odd_count] += 1

        return res

        