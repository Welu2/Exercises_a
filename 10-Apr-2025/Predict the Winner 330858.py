# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(left: int, right: int) -> int:
            if left == right:
                return nums[left]

            # Choose left or right, and subtract the result of the opponent's turn
            pick_left = nums[left] - helper(left + 1, right)
            pick_right = nums[right] - helper(left, right - 1)

            return max(pick_left, pick_right)

        return helper(0, len(nums) - 1) >= 0
        