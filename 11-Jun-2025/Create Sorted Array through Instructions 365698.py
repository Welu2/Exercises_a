# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        nums = []
        
        def insert_and_count(num):
            # Standard binary search insertion point
            left, right = 0, len(nums)
            less = greater = 0

            while left < right:
                mid = (left + right) // 2
                if nums[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            less = left

            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= num:
                    left = mid + 1
                else:
                    right = mid
            greater = len(nums) - left

            # Insert into the sorted list (like merge sort would do)
            nums.insert(left, num)
            return min(less, greater)

        total_cost = 0
        for num in instructions:
            cost = insert_and_count(num)
            total_cost = (total_cost + cost) % MOD

        return total_cost