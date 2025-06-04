# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def can_zero_with_k_queries(k):
            delta = [0] * (n + 1)
            for i in range(k):
                l, r, val = queries[i]
                delta[l] += val
                if r + 1 < n:
                    delta[r + 1] -= val

            available = [0] * n
            curr = 0
            for i in range(n):
                curr += delta[i]
                available[i] = curr

            for i in range(n):
                if nums[i] > available[i]:
                    return False
            return True

        left, right = 0, len(queries)
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if can_zero_with_k_queries(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer